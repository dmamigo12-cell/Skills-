"""Reproducible, dependency-free style measurements for Russian scientific prose.

Markdown/HTML scaffolding, displayed formulae and tables are excluded. Inline
formulae count as one token. Sentence length is a diagnostic, not authorship proof.
"""
import argparse
import collections
import html
import json
import re
import statistics
from pathlib import Path

WORD = re.compile(r"[A-Za-zА-Яа-яЁё0-9]+(?:[-‑][A-Za-zА-Яа-яЁё0-9]+)*")
LINKS = ['при этом', 'в этом случае', 'таким образом', 'для этого', 'в результате',
         'следовательно', 'однако', 'кроме того', 'рассмотрим', 'отметим',
         'позволяет', 'представляет собой', 'в качестве', 'за счет']

def paragraphs(raw):
    raw = re.sub(r'^---\s*\n.*?\n---\s*\n', '', raw, flags=re.S)
    raw = re.sub(r'```.*?```', '', raw, flags=re.S)
    raw = re.sub(r'<table\b.*?</table>', '', raw, flags=re.S | re.I)
    raw = re.sub(r'\$\$.*?\$\$', '', raw, flags=re.S)
    raw = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', raw)
    raw = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', raw)
    raw = raw.replace('\\[', '[').replace('\\]', ']')
    raw = re.sub(r'\[[\d\s,;–—-]+\]', '', raw)
    raw = re.sub(r'\$[^$\n]+\$', ' ФОРМУЛА ', raw)
    raw = re.sub(r'<[^>]+>', '', raw)
    raw = html.unescape(raw).replace('\xa0', ' ')
    raw = raw.replace('*', '').replace('`', '')
    out = []
    for block in re.split(r'\n\s*\n', raw):
        lines = [x.strip() for x in block.splitlines() if x.strip()]
        lines = [x for x in lines if not re.match(r'^(?:#|\||Рисунок\s+\d|Таблица\s+\d|\[\[)', x)]
        p = re.sub(r'\s+', ' ', ' '.join(lines)).strip()
        p = re.sub(r'^[-•]\s+', '', p)
        if not re.search(r'[А-Яа-яЁё]{3}', p.replace('ФОРМУЛА','')):
            continue
        if re.fullmatch(r'[\W\d]+', p):
            continue
        out.append(p)
    return out

def sentences(p):
    # Protect abbreviations and decimal / section numbers before splitting.
    p = re.sub(r'\b(?:т\s*\.\s*[ек]\.|рис\.|табл\.|англ\.|см\.)',
               lambda m: m.group().replace('.', '∯'), p, flags=re.I)
    p = re.sub(r'\b[A-Z]\.\s*(?=[A-Z](?:[a-z]|\.))', lambda m:m.group().replace('.', '∯'), p)
    p = re.sub(r'\b[А-ЯЁ]\.\s*(?=[А-ЯЁ](?:[а-яё]|\.))', lambda m:m.group().replace('.', '∯'), p)
    p = re.sub(r'(?<=\d)\.(?=\d)', '∯', p)
    p = re.sub(r'\.{2,}', '…', p)
    return [s.replace('∯', '.').strip() for s in re.split(r'(?<=[.!?])\s+', p)
            if WORD.search(s) and re.search(r'[А-Яа-яЁё]', s)]

def percentile(values, q):
    values = sorted(values)
    pos = (len(values)-1)*q
    lo = int(pos)
    hi = min(lo+1, len(values)-1)
    return round(values[lo] + (values[hi]-values[lo])*(pos-lo), 2)

def measure(raw, include_sentences=False):
    ps = paragraphs(raw)
    ss = [s for p in ps for s in sentences(p)]
    lengths = [len(WORD.findall(s)) for s in ss]
    if not lengths:
        return {'sentences': 0, 'words': 0, 'paragraphs': len(ps)}
    words = sum(lengths)
    joined = ' '.join(ps).lower()
    counts = {k: len(re.findall(r'(?<!\w)'+re.escape(k)+r'(?!\w)', joined)) for k in LINKS}
    result = {
        'paragraphs': len(ps), 'sentences': len(ss), 'words': words,
        'sentence_mean': round(statistics.mean(lengths), 2),
        'sentence_median': statistics.median(lengths),
        'sentence_p10': percentile(lengths,.1), 'sentence_p25': percentile(lengths,.25),
        'sentence_p75': percentile(lengths,.75), 'sentence_p90': percentile(lengths,.9),
        'sentence_p95': percentile(lengths,.95), 'sentence_max': max(lengths),
        'sentence_sd': round(statistics.pstdev(lengths),2),
        'sentences_under_8_pct': round(100*sum(x<8 for x in lengths)/len(ss),2),
        'sentences_over_40_pct': round(100*sum(x>40 for x in lengths)/len(ss),2),
        'sentences_12_30_pct': round(100*sum(12<=x<=30 for x in lengths)/len(ss),2),
        'words_per_paragraph_median': statistics.median([len(WORD.findall(p)) for p in ps]),
        'sentences_per_paragraph_median': statistics.median([len(sentences(p)) for p in ps]),
        'commas_per_sentence': round(sum(s.count(',') for s in ss)/len(ss),2),
        'semicolon_per_1000_words': round(1000*joined.count(';')/words,2),
        'colon_per_1000_words': round(1000*joined.count(':')/words,2),
        'dash_count': sum(joined.count(x) for x in ['—','–']),
        'connectors_counts': counts,
        'connectors_per_1000_words': {k: round(1000*v/words,2) for k,v in counts.items()},
        'subordination_per_1000_words': {k: round(1000*len(re.findall(pat,joined))/words,2)
            for k,pat in {'который':r'\bкотор\w*', 'что':r'\bчто\b', 'если':r'\bесли\b', 'чтобы':r'\bчтобы\b'}.items()},
        'starts_top': collections.Counter(' '.join(WORD.findall(s.lower())[:2]) for s in ss).most_common(12),
    }
    if include_sentences:
        result['sentence_records'] = [{'words':n,'text':s} for s,n in zip(ss,lengths)]
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('files', nargs='+', type=Path)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--sentences', action='store_true')
    args=ap.parse_args()
    rows={str(p):measure(p.read_text(encoding='utf-8-sig'),args.sentences) for p in args.files}
    rendered=json.dumps(rows,ensure_ascii=False,indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(rendered,encoding='utf-8')
    else:
        print(rendered)

if __name__=='__main__': main()
