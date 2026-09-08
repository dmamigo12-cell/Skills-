---
name: scientific-writing
description: Writing, revising, and reviewing scientific articles, reports, dissertation materials, and individual sections with emphasis on scientific rigor, technical accuracy, logical consistency, preservation of scientific meaning, claim-to-evidence alignment, and a developed engineering-scientific writing style. The primary scope is technical and engineering research, including telecommunications, signal processing, coding theory, machine learning, modeling, optimization, and computational experiments.
license: MIT
metadata:
  version: "0.6-style"
  status: "draft"
---

# Scientific Writing

## 1. Purpose

Use this skill for:

- writing scientific articles, reports, and dissertation materials;
- preparing individual sections such as abstracts, introductions, system models, problem statements, methods, algorithms, experimental sections, results, discussions, and conclusions;
- revising and rewriting existing scientific text;
- improving scientific logic and exposition;
- shortening scientific text when shortening is explicitly requested;
- scientific review of existing text;
- preparing responses to reviewers.

The goal is to produce text that:

1. is technically correct;
2. is logically consistent;
3. contains no fabricated facts;
4. does not overstate results;
5. separates facts, assumptions, observations, explanations, and inferences;
6. is consistent with formulas, figures, tables, numerical data, and source materials;
7. preserves the necessary scientific explanation and context;
8. develops the argument sufficiently for a reader to follow the scientific reasoning;
9. reads as a full technical scientific article rather than as a compressed technical summary;
10. is natural for Russian-language engineering and telecommunications research.

This file defines the general scientific-writing workflow.

For Russian-language scientific writing or revision, always read and apply:

- `references/CORE_STYLE.md`;
- `references/style-guide_ru.md`.

Scientific correctness always has priority over stylistic preferences.

For Russian-language technical articles, the target prose should be moderately detailed rather than minimalistic. The preferred model is a developed scientific narrative in which the reader is gradually led from the technical context to the problem, existing approaches, the proposed method, the experimental setup, and the interpretation of the results.

---

## 2. Instruction Priority

When instructions conflict, use the following priority:

1. explicit user request;
2. factual data and materials from the current study;
3. current project context;
4. rules defined in this skill;
5. `references/style-guide_ru.md` for Russian-language scientific text;
6. `references/CORE_STYLE.md`;
7. additional project-specific reference materials;
8. general model knowledge.

General model knowledge may help explain established concepts, but it must not be used as a source for specific results, parameters, claims, novelty, experimental conditions, or evidence belonging to the current study.

For Russian-language text, the requirements of `references/style-guide_ru.md` are mandatory unless they conflict with scientific correctness, this skill, or an explicit user instruction.

If a lower-priority style rule would make the text unnaturally short, fragmentary, or summary-like, preserve the scientific explanation and developed exposition required by this skill.

---

## 3. Core Scientific Rules

### 3.1. Do Not Fabricate Information

Do not invent or complete:

- experimental or simulation results;
- numerical values;
- simulation parameters;
- sample sizes;
- characteristics of systems or models;
- metric values;
- statistical results;
- algorithms or analysis steps;
- experimental conditions;
- software versions;
- references, DOIs, article titles, authors, or quotations;
- novelty claims;
- conclusions that do not follow from the available evidence.

If information is missing, mark it explicitly, for example:

- `[clarification required]`;
- `[data unavailable]`;
- `[not verified by source]`;
- `[source required]`.

Do not replace missing information with a plausible assumption unless the assumption is explicitly identified as such.

Do not use a stylistically convincing sentence to hide the absence of evidence.

### 3.2. Preserve Scientific Meaning

When revising or rewriting text, do not change its scientific meaning for the sake of style.

Preserve:

- definitions;
- notation;
- physical and mathematical meaning;
- causal relationships;
- assumptions;
- limitations;
- applicability conditions;
- uncertainty in the results;
- relevant explanation and motivation;
- distinctions between approaches;
- distinctions between experimental scenarios;
- distinctions between direct observations and interpretations.

If the original wording is scientifically questionable, identify the issue separately instead of hiding it through stylistic rewriting.

### 3.3. Calibrate Claims to Evidence

Every nontrivial scientific claim must be supported by at least one of:

- provided study data;
- an explicit local assumption;
- a derivation;
- a reported experiment or simulation;
- a verified external source.

Do not turn:

- correlation into causation;
- improvement in one metric into proof of overall superiority;
- simulation results into proof of real-world effectiveness;
- lack of statistical significance into proof of equivalence;
- performance in one scenario into a universal claim;
- a limited experiment into a general conclusion.

Performance comparisons should be scoped by:

- metric;
- comparison method or baseline;
- operating condition;
- magnitude or trend, when available.

### 3.4. Separate Observation from Explanation

Distinguish between:

**Observation / Result** - what is directly shown by the experiment, numerical data, figure, or table.

**Interpretation / Explanation** - a possible or supported reason for the observed result.

**Inference** - a conclusion derived from evidence or mathematical reasoning.

**Assumption** - a condition introduced by the study.

Do not present an interpretation or assumption as an established fact.

At the same time, do not omit interpretation entirely. A scientific article should normally explain the meaning of important results when the available evidence allows it.

### 3.5. Do Not Rewrite More Than Necessary

For local edits, modify only the necessary fragments.

Do not rewrite an entire section, article, or document unless the user explicitly asks for it or a broader rewrite is required to fix a logical or structural problem.

Preserve strong original wording when it is scientifically correct and stylistically appropriate.

---

## 4. Rewriting Is Not Shortening

A request to rewrite, improve, polish, revise, or make a text more scientific does not imply a request to shorten it.

When rewriting an existing scientific text:

- preserve its substantive coverage;
- preserve the depth of the literature discussion;
- preserve useful explanations;
- preserve methodological reasoning;
- preserve mathematical motivation;
- preserve experimental conditions;
- preserve discussion of results;
- preserve limitations;
- preserve meaningful distinctions between approaches and scenarios;
- preserve citations and their relation to claims.

Do not compress several scientifically distinct paragraphs into one merely because the combined information can be stated more briefly.

Do not automatically remove background material if it performs a real scientific function in the argument.

Do not replace a developed scientific explanation with a short declarative statement solely for concision.

By default, keep the rewritten text roughly comparable in length and informational depth to the source. A useful practical target is approximately 90-110% of the original substantive text, unless:

- the user explicitly requests shortening or expansion;
- the source contains clear duplication;
- the source contains obvious filler;
- the source contains material that is scientifically irrelevant;
- structural correction requires redistribution of material.

This range is not a mechanical quota. Its purpose is to prevent accidental summarization.

If the rewritten version becomes substantially shorter than the source, perform a dedicated check for lost explanation, literature context, methodological detail, experimental conditions, and result interpretation before returning it.

---

## 5. Target Style for Russian Technical Articles

For Russian-language engineering articles, use a developed and explanatory scientific style.

The target text should typically have the following characteristics:

- paragraphs contain several logically connected sentences rather than isolated statements;
- a technical idea is introduced, explained, and then connected to its consequence;
- difficult points receive more explanation than obvious ones;
- the Introduction may be relatively detailed if it is needed to establish the technical context;
- the literature review explains differences between approaches instead of only citing them;
- mathematical expressions are integrated into the narrative;
- method sections explain why major steps are required;
- results sections explain what was observed and what the result means;
- key technical terms may repeat when repetition improves clarity;
- standard scientific transitions are allowed when they reflect the actual logic of the argument.

Do not optimize the manuscript for maximum information density.

Do not aim for a sequence of uniformly short paragraphs.

Do not make every sentence equally short or structurally identical.

Do not remove a scientifically useful explanation simply because a specialist could infer it from the surrounding equations.

The final manuscript should read as a complete technical study written by researchers for other researchers, not as an automatically generated summary of the study.

---

## 6. Input Information

Before writing new text or rewriting existing text, determine which materials are available.

When relevant, use:

- document type and purpose;
- target audience;
- language;
- target journal or conference;
- existing manuscript context;
- problem statement;
- system or mathematical model;
- methods;
- assumptions;
- results;
- tables and figures;
- source numerical data;
- bibliography;
- length requirements;
- existing terminology and notation.

If information is incomplete, work only within the available evidence.

Do not request unnecessary materials when the current information is sufficient for the specific task.

When rewriting a source document, treat its scientific content, organization, level of detail, cited evidence, and explanatory depth as the default basis unless the user explicitly requests substantive restructuring.

---

## 7. Working Modes

### 7.1. Writing New Text

Create text only from provided or verified information.

Do not add new scientific facts, parameters, references, or conclusions without evidence.

When enough information is available, develop the scientific argument sufficiently for the reader to understand:

- what problem is being considered;
- why the problem matters;
- what technical principles are required to understand it;
- which approaches already exist;
- why the chosen method is introduced;
- what each major step of the method does;
- how the experiment is organized;
- what the results show;
- how the results should be interpreted;
- what limitations remain.

Writing new text is not the same as producing a compressed synthesis of the available facts.

### 7.2. Revising or Rewriting Existing Text

Improve the existing text while preserving its scientific meaning, substantive coverage, and useful explanatory depth.

Check:

- accuracy;
- coherence;
- terminology;
- structure;
- unsupported claims;
- unnecessary repetition;
- scientific style;
- preservation of relevant details;
- preservation of literature logic;
- preservation of methodological explanation;
- preservation of result interpretation;
- preservation of section depth.

For Russian-language text, apply both `references/CORE_STYLE.md` and `references/style-guide_ru.md`.

Do not treat every repeated technical term as redundancy. Repetition is acceptable when it is required for clarity, continuity, or unambiguous reference to the same technical object.

Do not automatically merge paragraphs that perform different scientific functions.

When the original article already has a developed and coherent argument, prefer careful paragraph-level revision over aggressive restructuring.

### 7.3. Scientific Review

Evaluate separately:

1. scientific correctness;
2. logical consistency;
3. completeness of the problem statement;
4. consistency between methods and results;
5. justification of conclusions;
6. correctness of terminology;
7. sufficiency of experimental description;
8. consistency among text, formulas, tables, and figures;
9. adequacy of scientific explanation;
10. whether important context was removed or compressed excessively.

A scientific problem must not be hidden by stylistic rephrasing.

### 7.4. Shortening Text

Shortening is a separate mode and should be used only when explicitly requested.

Preserve:

- the main scientific idea;
- necessary conditions;
- key results;
- limitations;
- causal relationships;
- enough explanation to keep the argument understandable.

Remove first:

- exact repetition;
- empty introductory phrases;
- duplicated information;
- stylistic padding that does not support the scientific argument.

Do not remove:

- distinct literature positions;
- methodological justification;
- explanation of variables or assumptions;
- experimental conditions required for interpretation;
- important discussion of mechanisms or limitations.

---

## 8. Plan Before Drafting

Before drafting a substantial section, create a short internal paragraph plan.

For each planned paragraph identify:

1. its dominant scientific or rhetorical function;
2. the evidence, result, equation, or idea it will use;
3. the explanation or context required for the reader;
4. its logical relation to the previous paragraph.

A paragraph plan may contain, for example:

`P1: broad technical context and relevance`  
`P2: necessary background on the technology`  
`P3: practical limitation of the standard formulation`  
`P4: first family of existing approaches and its limitation`  
`P5: second family of approaches and remaining issue`  
`P6: proposed idea and motivation`  
`P7: evaluation scenarios and main contribution`

Do not force the final text into a rigid template.

Do not merge planned paragraphs solely because they concern the same general topic.

The plan is working state and should not appear in the final manuscript unless the user asks for it.

---

## 9. Structure of Scientific Text

The structure must match the document type and scientific task.

For a technical scientific article, a typical structure is:

1. Introduction.
2. System Model / Problem Statement.
3. Proposed Method or Algorithm.
4. Simulation or Experimental Setup.
5. Results and Discussion.
6. Conclusion.

Other structures are acceptable when they better match the study.

IMRAD is not mandatory.

Each paragraph should have one dominant scientific function, but it may also contain supporting explanation, technical detail, qualification, and a natural logical transition.

Do not reduce a section to a sequence of bare technical statements.

---

## 10. Abstract

The abstract should normally contain:

1. the problem or scenario;
2. the proposed method or investigated approach;
3. the main technical principle;
4. the evaluation scenario;
5. the main quantitative or qualitative result;
6. the practical or scientific implication, when justified.

The abstract should be compact relative to the article, but it should not become a list of telegraphic phrases.

Do not include unsupported promotional claims.

Do not introduce details that are absent from the article.

If the article includes several distinct experimental scenarios that are central to the contribution, they may be mentioned explicitly rather than collapsed into a vague statement such as “different conditions were considered.”

---

## 11. Introduction

The Introduction is not merely a short lead-in. In a technical article it may perform a substantial part of the scientific argument.

The Introduction should normally establish, in a gradual sequence:

1. the broader technical problem;
2. the relevant technology or scientific principle;
3. the specific mechanism relevant to the study;
4. the practical condition under which the standard approach becomes insufficient;
5. existing approaches to this condition;
6. differences between these approaches;
7. their concrete limitations;
8. the unresolved issue addressed by the current work;
9. the proposed approach;
10. the scope of evaluation and main contribution.

Do not state the contribution before the reader has enough technical context to understand why it is needed.

Do not rush from general background directly to the proposed method if intermediate technical explanation is necessary.

### 11.1. Background in the Introduction

Background material is appropriate when it is necessary to understand the problem.

For example, it may be useful to explain:

- the principle of the considered coding or signal-processing method;
- why a certain quantity determines system behavior;
- why a standard construction assumes particular channel conditions;
- how practical conditions violate those assumptions.

Do not remove such material merely because it is established knowledge.

At the same time, avoid generic background that could be copied into almost any paper in the field.

### 11.2. Literature Review in the Introduction

The literature review should be analytical rather than decorative.

When appropriate:

- divide previous work into technical directions;
- explain the basic principle of each direction;
- identify representative works;
- preserve differences between individual approaches when those differences matter;
- explain the limitation relevant to the current study;
- connect the limitation to the proposed method.

It is acceptable to discuss an individual paper in a separate sentence or paragraph when its method or limitation has a distinct role in the argument.

Do not force all references into one highly compressed synthesis.

Do not reduce several technically different approaches to a single sentence merely to save space.

Do not write a paper-by-paper list when the works genuinely form one technical family.

Choose the level of synthesis that best preserves the scientific logic.

### 11.3. Research Gap and Contribution

Do not manufacture an artificial research gap.

The need for the current work should follow naturally from the technical limitations already described.

State contributions in concrete and verifiable terms.

Prefer formulations such as:

- “a method is proposed...”;
- “an algorithm is developed...”;
- “a scenario is considered...”;
- “the dependence of ... is investigated...”;
- “a comparison is performed...”;
- “the method is verified by...”;
- “a reduction in ... is obtained under ...”.

Do not use “novel”, “unique”, “revolutionary”, or equivalent terms without strong evidence.

Novelty claims require literature support.

### 11.4. End of the Introduction

The final part of the Introduction may briefly describe:

- what method is proposed;
- what problem it addresses;
- how it is evaluated;
- which experimental scenarios are considered;
- the principal supported result.

This summary should complete the argument rather than merely repeat the abstract.

---

## 12. System Model and Problem Statement

The system model should give the reader enough information to understand the physical and mathematical setting before the proposed method is introduced.

Make clear:

- what system is considered;
- what signals are transmitted;
- which objects correspond to physical resources;
- what is known at the transmitter and receiver;
- what is estimated;
- what is fixed;
- what varies between channel realizations or experiments;
- which assumptions are used;
- what performance criterion is relevant.

For communication-system papers, pay particular attention when relevant to:

- transmission direction;
- direct and feedback channels;
- pilot transmission;
- channel estimation;
- CSI availability;
- compression and reconstruction;
- mapping of coded bits to resources;
- equalization;
- modulation;
- coding and decoding assumptions;
- duplex mode;
- comparison conditions.

Introduce assumptions before using them.

Do not introduce a large set of symbols before the reader understands the physical meaning of the model.

---

## 13. Formulas and Notation

Use notation consistently throughout the document.

Define a variable when it first appears unless its meaning is genuinely obvious to the target audience.

Check:

- dimensions;
- indices;
- transposition and conjugation;
- norms;
- expectations;
- units;
- domains;
- normalization;
- consistency between text and equations.

Do not use different symbols for the same object without a reason.

Do not use the same symbol for different objects.

For important equations, prefer the sequence:

`physical or mathematical context -> motivation -> equation -> definition of new symbols -> interpretation or next step`

Not every equation requires a long explanation, but every important equation should have a clear role in the argument.

Do not place several major equations consecutively without enough prose to explain how they are related.

Do not fully restate an equation in words unless doing so adds understanding.

When rewriting, preserve useful explanation around equations even if the formula itself appears self-explanatory to a specialist.

---

## 14. Methods and Algorithms

A method section should communicate the scientific idea, not only the operational sequence.

Before presenting the algorithm, explain:

- what exact problem remains after the system model;
- why direct optimization or exhaustive search is impractical, if relevant;
- why the proposed criterion is introduced;
- how the criterion relates to the actual performance metric;
- what property of the system structure is used by the algorithm.

For each major algorithmic step, explain when the information is available:

1. what is selected or calculated;
2. why this operation is performed;
3. how it relates to the objective;
4. what condition determines acceptance or rejection;
5. how the process continues or stops.

If the algorithm contains several stages, a numbered list is acceptable, but the surrounding scientific explanation should not be reduced to the list alone.

If the method includes:

- an approximation;
- a relaxation;
- a heuristic;
- an equivalent transformation;
- a surrogate objective;
- a bound;
- a greedy search;

name its mathematical status correctly.

Do not call a heuristic an exact optimization method.

Do not claim global optimality unless it is proved or verified under the stated conditions.

### 14.1. Complexity

If computational complexity is part of the contribution:

- identify the dominant operations;
- state what variables the complexity depends on;
- distinguish offline and online complexity when relevant;
- connect the complexity discussion to the intended operating scenario.

Do not state that a method is practical for real-time use solely from an asymptotic expression unless the available evidence supports that interpretation.

---

## 15. Experiments and Metrics

Experimental conditions must be sufficient for correct interpretation of the results.

When relevant, specify:

- model or channel type;
- code length and rate;
- modulation;
- decoder;
- list size;
- CRC;
- number of channel realizations;
- number of random initializations or permutations;
- number of transmitted codewords;
- SNR or Eb/N0 range;
- comparison methods;
- whether parameters or templates are reoptimized between scenarios.

Do not remove these details simply because they make the paragraph longer.

Each metric must be:

1. defined;
2. correctly denoted;
3. appropriate for the task;
4. calculated consistently across compared methods.

When comparing methods, make sure the operating conditions are genuinely comparable.

If they are not, state the difference explicitly.

---

## 16. Results and Discussion

Results should be developed as scientific analysis, not as captions rewritten into prose.

For each important figure, table, or experiment, consider the following sequence:

1. remind the reader of the experimental condition if needed;
2. state what is being compared;
3. identify the main observed trend;
4. provide the important numerical difference when available;
5. explain what changes between scenarios;
6. interpret the result;
7. state the limitation of the interpretation when relevant.

Not every result requires all seven steps, but important results often require more than one sentence.

Do not reproduce every numerical point from a graph.

Do not reduce an important graph to a single sentence such as “the proposed method performs better.”

### 16.1. Interpretation

Discussion should explain the scientific meaning of the result.

Useful discussion may include:

- why the observed trend is expected from the model;
- why the difference between methods changes with the operating condition;
- why a method remains effective when the channel model changes;
- what the result says about robustness;
- what the result does not establish.

If the explanation is a hypothesis rather than a demonstrated mechanism, state it cautiously.

### 16.2. Multiple Experimental Scenarios

When several scenarios are studied, preserve their distinct scientific roles.

For example, one scenario may:

- verify the criterion against exhaustive search;

another may:

- demonstrate performance at a practical code length;

another may:

- test robustness to a different channel distribution.

Do not collapse such scenarios into one generic sentence about “various conditions.”

### 16.3. Figures

A single important figure may require:

- one paragraph describing the setup and observation;
- another paragraph interpreting the result;
- another paragraph explaining a limitation or comparison.

This is acceptable when each paragraph adds scientific value.

---

## 17. Working with Literature

A source must genuinely support the claim for which it is cited.

Do not:

- fabricate bibliographic entries;
- reconstruct DOIs from memory;
- cite an unverified or nonexistent source;
- use an article title as evidence for detailed content;
- treat a search snippet as confirmation of a claim.

Attach citations to specific external claims.

When discussing multiple works, synthesize them by technical idea when that preserves the logic.

However, do not merge distinct works so aggressively that important methodological differences disappear.

If one work provides a specific counterexample, limitation, or alternative principle relevant to the current argument, preserve that distinction.

When a source is missing, use:

`[source required]`

Treat literature search and scientific writing as related but separate stages.

---

## 18. Scientific Style

For Russian-language scientific writing or revision, always follow:

- `references/CORE_STYLE.md`;
- `references/style-guide_ru.md`.

These references define detailed Russian-language stylistic preferences.

The following higher-level requirements apply regardless of those files:

- do not aim for maximum compression;
- do not turn developed paragraphs into short summaries;
- do not remove scientific explanation merely because it is inferable;
- use stable technical terminology;
- allow natural repetition of key terms;
- allow standard scientific transitions when they have a real logical function;
- avoid promotional language;
- avoid artificial sophistication;
- avoid a monotonous sequence of short declarative sentences.

Standard Russian scientific phrases are not forbidden by default.

Phrases such as:

- «В настоящей работе...»
- «Вместе с тем...»
- «Таким образом...»
- «Для оценки эффективности...»
- «Полученные результаты показывают...»

may be used when they naturally perform a logical function.

The problem is mechanical repetition, not the existence of the phrase itself.

Do not replace every standard scientific construction with an artificially terse alternative.

---

## 19. Tables, Figures, and Numerical Data

Text, tables, figures, and formulas must be mutually consistent.

Check:

- notation;
- units;
- numerical values;
- experimental conditions;
- captions;
- axes;
- abbreviations.

Do not duplicate an entire table or figure in the text.

Use prose to explain the scientifically important observation, comparison, trend, or implication.

If a figure has several important aspects, discuss them separately rather than compressing them into one sentence.

---

## 20. Conclusion

The Conclusion should normally:

- restate the scientific problem briefly;
- identify the proposed or applied approach;
- summarize the major supported results;
- state the demonstrated scope of applicability;
- mention limitations or future work when appropriate.

Do not:

- introduce new results;
- introduce new literature;
- repeat the Introduction;
- make conclusions broader than the evaluated scope.

The Conclusion should be more compact than the main text, but it should still read as a coherent scientific synthesis rather than a list of isolated outcomes.

A final sentence about practical applicability or prospects is acceptable only when it follows from the reported results.

---

## 21. Working with Incorrect or Ambiguous Text

If the source text may contain a scientific error:

1. do not hide it through editing;
2. identify the problem;
3. explain why the wording may be incorrect;
4. propose a correction only within the limits of the available information.

If several interpretations are possible, state them explicitly.

Do not shorten ambiguous material in a way that removes the ambiguity from the wording while leaving the scientific problem unresolved.

---

## 22. Responses to Reviewers

When preparing responses to reviewers:

- state what was changed;
- explain the technical reason;
- identify where the change was made;
- keep the tone professional and calm.

Do not use excessive gratitude or defensive language.

Do not accept a requested scientific change if it would introduce an unsupported claim.

---

## 23. Final Self-Check

Before returning scientific text, verify the following.

### Scientific Meaning

- Were any unsupported facts added?
- Do all conclusions follow from the available evidence?
- Was the meaning of the source text preserved?
- Were advantages overstated?
- Were important limitations preserved?
- Was useful explanation removed?

### Claim and Evidence Alignment

- Does every nontrivial claim have a basis?
- Are performance claims scoped by metric, comparison method, and operating condition?
- Is novelty supported by literature?
- Are observation and explanation distinguished?

### Logic and Structure

- Is the problem statement understandable before the method is introduced?
- Does the method follow logically from the problem?
- Does each paragraph have a meaningful scientific function?
- Are supporting explanations present where needed?
- Are logical prerequisites introduced before dependent claims?
- Were distinct literature directions merged excessively?
- Were distinct experimental scenarios merged excessively?

### Technical Consistency

- Is notation consistent?
- Are central symbols defined?
- Do numerical values match?
- Are units consistent?
- Are metrics defined correctly?
- Are text, formulas, tables, and figures aligned?

### Mathematical Exposition

- Are important equations motivated?
- Are new symbols defined?
- Is the role of each major equation understandable?
- Are assumptions introduced before use?
- Is there enough prose between major equations?

### Rewrite Fidelity

When rewriting an existing text:

- Is the rewritten article similar in substantive coverage to the source?
- Is the section depth preserved?
- Was the Introduction compressed?
- Was the literature review compressed?
- Were methodological explanations removed?
- Were experimental details removed?
- Were result interpretations removed?
- Did rewriting accidentally become summarization?
- Did several developed paragraphs become one short paragraph without a scientific reason?

### Target Russian Style

For Russian-language technical articles:

- Does the text use developed paragraphs rather than a telegraphic style?
- Is the argument introduced gradually?
- Is the literature review explanatory rather than decorative?
- Are formulas integrated into the narrative?
- Is the method explained in terms of both operations and motivation?
- Are important results discussed rather than merely stated?
- Are standard scientific transitions used naturally rather than mechanically?
- Does the text read like a complete journal article rather than a technical note or summary?

### Sources

- Are sources provided where required?
- Were any references fabricated?
- Does each source actually support the corresponding claim?

If a scientific uncertainty or evidence gap is identified, report it separately instead of hiding it inside the revised text.

---

## 24. Core Principle

The quality of scientific writing is determined not by minimum length and not by maximum density, but by the precision, completeness, and clarity of the scientific thought.

Remove filler, repetition, and empty wording.

Preserve technical background when it is needed to understand the problem.

Preserve explanation when it clarifies the method.

Preserve discussion when it explains the meaning of the results.

When brevity conflicts with scientific context, methodological reasoning, or interpretation, preserve the scientific depth.
