"""Measure style and report review signals; never declare authorial identity."""
import argparse
import json
import re
from pathlib import Path
from analyze_style import measure

def check(raw, reference=None):
    m=measure(raw,True)
    signals=[]
    prose=' '.join(x['text'] for x in m.get('sentence_records',[]))
    if m['words']<300: signals.append('Short sample: distributional comparisons are unstable.')
    limits={'sentence_mean':(15,21),'sentence_median':(14,20),'sentence_p90':(24,34),'sentence_sd':(5,10.5),
            'sentences_under_8_pct':(0,10),'sentences_over_40_pct':(0,2)}
    if m['sentences']:
        for k,(lo,hi) in limits.items():
            if not lo<=m[k]<=hi: signals.append(f'Review {k}: {m[k]} outside orientation {lo}..{hi}.')
    if re.search(r'[—–]|\s-\s',prose):
        signals.append('Review dashes: replace punctuation dashes through syntax; preserve mathematical signs and term hyphens.')
    suspects=[r'не претенду\w*',r'не следует воспринимать',r'всего лишь',r'не [^.!?]{1,100}, а (?:лишь |только )?']
    m['rhetoric_review_matches']=[match.group() for pat in suspects for match in re.finditer(pat,prose,re.I)]
    if m['rhetoric_review_matches']: signals.append('Review contrasting/apologetic wording in context; do not delete technical negatives automatically.')
    for k,count in m.get('connectors_counts',{}).items():
        if k in ['при этом','в этом случае','таким образом','отметим','рассмотрим','для этого','однако','кроме того'] and count>2 and count*500/max(m['words'],1)>2:
            signals.append(f'Repeated connector: {k} ({count} occurrences).')
    result={'metrics':m,'review_signals':signals,'verdict':'Manual semantic and stylistic review required.'}
    if reference is not None:
        ref=measure(reference)
        delta={k:round(m[k]-ref[k],2) for k in ['sentence_mean','sentence_median','sentence_p90','commas_per_sentence']}
        ratio=round(m['sentence_sd']/ref['sentence_sd'],3) if ref['sentence_sd'] else None
        result['reference_metrics']=ref
        result['comparison']={'deltas':delta,'sd_ratio':ratio,
            'project_numeric_criteria_met':abs(delta['sentence_mean'])<=3 and abs(delta['sentence_median'])<=3 and abs(delta['sentence_p90'])<=5 and abs(delta['commas_per_sentence'])<=.6 and ratio is not None and .65<=ratio<=1.45}
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument('text',type=Path)
    p.add_argument('--reference',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    report=check(args.text.read_text(encoding='utf-8-sig'),args.reference.read_text(encoding='utf-8-sig') if args.reference else None)
    value=json.dumps(report,ensure_ascii=False,indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(value,encoding='utf-8')
    else: print(value)

if __name__=='__main__': main()
