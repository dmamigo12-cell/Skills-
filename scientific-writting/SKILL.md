---
name: scientific-writing
description: Writing, revising, and reviewing scientific articles, reports, and individual sections with emphasis on scientific rigor, technical accuracy, logical consistency, claim-to-evidence alignment, preservation of scientific meaning, and consistency with source data. The primary scope is technical and engineering research, including telecommunications, signal processing, machine learning, modeling, and computational experiments.
license: MIT
metadata:
  version: "0.5-en"
  status: "draft"
---

# Scientific Writing

## 1. Purpose

Use this skill for:

- writing scientific articles, reports, and dissertation materials;
- preparing individual sections such as abstracts, introductions, problem statements, methods, results, discussions, and conclusions;
- revising and rewriting scientific text;
- shortening scientific text when explicitly requested;
- scientific review of existing text;
- preparing responses to reviewers.

The goal is to produce text that:

1. is technically correct;
2. is logically consistent;
3. contains no fabricated facts;
4. does not overstate results;
5. separates facts, assumptions, results, interpretations, and inferences;
6. is consistent with formulas, figures, tables, and source data;
7. preserves the necessary scientific explanation and context;
8. is readable, natural, and professionally scientific.

This file defines the general scientific-writing workflow.

For Russian-language scientific writing or revision, always read and apply:

- `references/CORE_STYLE.md`;
- `references/style-guide_ru.md`.

Scientific correctness always has priority over stylistic preferences.

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

General model knowledge may help explain concepts, but it must not be used as a source for specific results, parameters, claims, novelty, or evidence belonging to the current study.

For Russian-language text, the requirements of `references/style-guide_ru.md` are mandatory unless they conflict with scientific correctness or an explicit user instruction.

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
- important distinctions between approaches, scenarios, and results.

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
- baseline;
- operating condition;
- magnitude or trend, when available.

### 3.4. Separate Observation from Explanation

Distinguish between:

**Observation / Result** - what is directly shown by the data, experiment, figure, or table.

**Interpretation / Explanation** - a possible reason for the observed result.

**Inference** - a conclusion derived from evidence or mathematical reasoning.

**Assumption** - a condition introduced by the study.

Do not present an interpretation or assumption as an established fact.

### 3.5. Do Not Rewrite More Than Necessary

For local edits, modify only the necessary fragments.

Do not rewrite an entire section, article, or document unless the user explicitly asks for it or a broader rewrite is required to fix a logical or structural problem.

Preserve strong original wording when it is scientifically correct and stylistically appropriate.

### 3.6. Rewriting Is Not Shortening

A request to rewrite, improve, polish, revise, or make a text more scientific does not imply a request to shorten it.

When rewriting an existing scientific text:

- preserve its substantive coverage;
- preserve useful explanations;
- preserve relevant literature context;
- preserve methodological reasoning;
- preserve discussion of results and limitations;
- preserve distinctions between different approaches or experimental scenarios.

Do not compress several scientifically distinct paragraphs into one merely because the combined text can be made shorter.

By default, keep the rewritten text roughly comparable in length and informational depth to the source. A practical target is approximately 90-110% of the original length, unless:

- the user explicitly asks for shortening or expansion;
- the source contains clear repetition;
- the source contains obvious filler;
- structural correction requires redistribution of material.

Removing redundancy is allowed. Removing explanation, motivation, methodological detail, or discussion solely for concision is not.

---

## 4. Scope

This skill is primarily intended for technical and engineering research involving:

- telecommunications;
- signal processing;
- machine learning;
- modeling;
- computational experiments;
- optimization;
- algorithm analysis.

It may also be used in other scientific fields when the task does not require domain-specific rules absent from this skill.

---

## 5. Input Information

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
- length requirements.

If information is incomplete, work only within the available evidence.

Do not request unnecessary materials when the current information is sufficient for the specific task.

When rewriting a source document, treat its scientific content, organization, level of detail, and cited evidence as the default basis unless the user explicitly asks for structural or substantive changes.

---

## 6. Working Modes

### 6.1. Writing New Text

Create text only from provided or verified information.

Do not add new scientific facts, parameters, references, or conclusions without evidence.

When enough information is available, include sufficient explanation for the reader to understand:

- why the problem matters;
- why the chosen method is used;
- what each major step does;
- how the results should be interpreted;
- what the limitations are.

Do not replace explanation with compressed statements solely to make the text shorter.

### 6.2. Revising or Rewriting Existing Text

Improve the existing text while preserving its scientific meaning, substantive coverage, and useful explanatory depth.

Check:

- accuracy;
- coherence;
- terminology;
- structure;
- repetition;
- unsupported claims;
- scientific style;
- preservation of relevant details;
- preservation of literature logic;
- preservation of methodological explanation;
- preservation of result interpretation.

For Russian-language text, apply both `references/CORE_STYLE.md` and `references/style-guide_ru.md`.

Do not treat every repeated technical term as redundancy. Repetition is acceptable when it is required for clarity, continuity, or correct reference to the same technical object.

Do not automatically merge paragraphs that perform different scientific functions.

### 6.3. Scientific Review

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

### 6.4. Shortening Text

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
- obvious statements;
- empty introductory phrases;
- duplicated information already shown in tables or figures;
- stylistic padding that does not support the scientific argument.

Do not remove:

- distinct literature positions;
- methodological justification;
- explanation of variables or assumptions;
- experimental conditions required for interpretation;
- important discussion of mechanisms or limitations.

---

## 7. Plan Before Drafting

Before drafting a substantial section, create a short internal paragraph plan.

For each planned paragraph identify:

1. its dominant scientific or rhetorical function;
2. the evidence, result, equation, or idea it will use;
3. supporting explanation or context that must be preserved;
4. its logical relation to the previous paragraph.

Example:

`P1: problem context - verified background and why it matters`  
`P2: prior approaches - main technical families and their limits`  
`P3: unresolved issue - specific limitation relevant to the current task`  
`P4: proposed approach - current study contribution and rationale`

Do not create a paragraph merely because a template suggests one.

Do not merge paragraphs solely because they refer to the same evidence. Merge them only if they perform the same scientific function and no explanatory depth is lost.

The plan is working state and should not appear in the final manuscript unless the user asks for it.

---

## 8. Structure of Scientific Text

The structure must match the document type and task.

For a technical scientific article, use the following structure by default:

1. Introduction.
2. Problem Statement / System Model.
3. Proposed Method.
4. Simulation or Experimental Setup.
5. Results.
6. Discussion.
7. Conclusion.

IMRAD is not mandatory when the nature of the work requires a different structure.

Each paragraph should have one dominant scientific function, but it may also contain supporting explanation, motivation, qualifications, and a natural transition when these help the reader understand the argument.

Do not reduce a section to a sequence of bare technical statements.

Avoid paragraphs that exist only for document-management phrases or generic significance statements.

---

## 9. Introduction

The Introduction should establish, in a logical sequence:

1. the problem;
2. its importance;
3. existing approaches;
4. a concrete limitation or unresolved issue;
5. the task addressed in the current work;
6. the specific contribution.

Do not state contributions before the reader understands the problem and why existing capability is insufficient.

A separate “research gap” paragraph is not mandatory when the gap is already clear from the limitation-to-proposal transition.

Avoid generic openings and artificial research gaps.

When rewriting an existing Introduction:

- preserve distinct literature directions when they support different technical ideas;
- preserve important differences between previous approaches;
- preserve the explanation of why a limitation matters;
- do not reduce a meaningful literature analysis to a short list of citations;
- do not collapse several technically distinct prior works into one sentence if their distinctions are relevant to the argument.

### Contribution of the Work

State contributions in concrete and verifiable terms.

Do not use the following without sufficient evidence:

- “novel”;
- “unique”;
- “revolutionary”;
- “significantly outperforms”;
- “substantially improves”;
- “effectively solves the problem”.

Prefer formulations such as:

- “a method is proposed...”;
- “a scenario is considered...”;
- “the dependence of ... is investigated...”;
- “a comparison is performed...”;
- “a reduction in ... is demonstrated under ...”.

Novelty claims require literature evidence.

---

## 10. Problem Statement and Methods

The description of the study should make clear:

- what is being considered;
- which objects and data are used;
- what is known to each side;
- which assumptions and constraints are imposed;
- what problem is being solved;
- which methods are used;
- which parameters materially affect the result.

For algorithms and ML models, include when applicable:

- input and output data;
- architecture;
- loss function;
- training procedure;
- testing procedure;
- normalization;
- metrics;
- baseline methods;
- key hyperparameters.

State assumptions before they are used.

Do not discuss a solution method before the objective, variables, constraints, and relevant difficulty are understandable.

Do not add missing parameters on your own.

When describing an algorithm, preserve not only the sequence of operations but also the scientific reason for important steps when that reason is available.

A technically correct method section should usually explain both:

- what is done;
- why it is done.

Do not reduce a method to an instruction list when the source contains meaningful mathematical or physical explanation.

---

## 11. Formulas and Notation

Use notation consistently.

Define a variable when it first appears unless its meaning is obvious from context.

Check:

- dimensions;
- indices;
- transposition and conjugation;
- norms;
- expectation;
- units;
- domains;
- normalization.

Do not use different symbols for the same object without a reason, and do not use the same symbol for different objects.

For major equations, prefer the sequence:

`orient or motivate -> equation -> define or qualify -> interpret or reuse`

Do not introduce major equations without explaining their role.

Do not fully restate a formula in words unless doing so adds understanding.

Do not remove explanatory text around equations solely to make the section shorter.

---

## 12. Experiments and Metrics

Experimental conditions must be sufficient for correct interpretation of the results.

Check:

- data and models;
- key system parameters;
- training and test sets;
- comparison conditions;
- baseline methods;
- consistency of conditions across compared methods;
- number of runs, when relevant;
- metrics used.

Each metric must be:

1. defined;
2. correctly denoted;
3. appropriate for the task;
4. calculated consistently for all compared methods.

Do not change a metric definition between sections.

If methods are compared under different conditions, state this explicitly.

When rewriting an experimental section, preserve conditions required for reproducibility and interpretation even if they make the text longer.

---

## 13. Results and Discussion

Results should describe what is directly observed.

For a comparison, include when available:

1. what is compared;
2. metric;
3. baseline;
4. operating condition;
5. magnitude or trend;
6. interpretation or explanation, if justified;
7. limitation or scope of the interpretation, when relevant.

Do not reproduce every value from a figure or table in prose.

Do not write vague statements such as “the proposed method demonstrates its effectiveness” without specifying what was measured and under which conditions.

Separate:

- figure/table pointer;
- observation;
- quantitative comparison;
- explanation;
- bounded implication.

Do not present an unverified mechanism as the reason for a result.

When rewriting results:

- preserve important experimental context;
- preserve meaningful comparisons;
- preserve explanations that help interpret the trends;
- preserve discussion of transferability, robustness, or limitations when supported by the study;
- do not reduce each figure to one sentence if the source contains a meaningful scientific discussion.

Discussion should add interpretation, mechanism, applicability, or limitation. It should not merely repeat the numerical result.

---

## 14. Working with Literature

A source must genuinely support the claim for which it is cited.

Do not:

- fabricate bibliographic entries;
- reconstruct DOIs from memory;
- cite an unverified or nonexistent source;
- use an article title as evidence for its content;
- treat a search snippet as confirmation of a claim.

Attach citations to specific external claims.

When discussing multiple works, synthesize them by technical idea or family when appropriate instead of narrating papers one by one.

However, do not merge distinct works so aggressively that important methodological differences or limitations disappear.

When a source is missing, use:

`[source required]`

Treat literature search and scientific writing as related but separate stages.

---

## 15. Scientific Style

For Russian-language scientific writing or revision, always follow:

- `references/CORE_STYLE.md`;
- `references/style-guide_ru.md`.

These references are mandatory for Russian-language output and define:

- general scientific style;
- personal stylistic preferences;
- Russian-language terminology choices;
- anti-LLM writing requirements.

Interpret requirements for brevity as removal of filler and redundancy, not as a requirement to minimize length.

A good scientific text may contain explanatory sentences that do not introduce a new result but help:

- motivate a method;
- clarify a causal relation;
- connect mathematical steps;
- interpret a result;
- explain why a limitation matters.

Do not remove such sentences solely because the text can technically be understood without them.

If these files conflict with scientific correctness or an explicit user instruction, follow scientific correctness and the explicit user instruction.

For non-Russian scientific text, use the general rules in this skill unless language-specific style instructions are provided.

---

## 16. Tables, Figures, and Numerical Data

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

Use prose to highlight the scientifically important observation, comparison, explanation, or implication.

A figure discussion may contain more than one sentence when several scientifically meaningful observations need to be explained.

---

## 17. Conclusion

The Conclusion should:

- briefly restate the problem;
- identify the proposed or applied approach;
- summarize the main supported results;
- mention limitations or future work when appropriate.

Do not:

- introduce new results;
- introduce new literature;
- repeat the Introduction;
- make conclusions broader than the evaluated scope.

The Conclusion should be concise relative to the main text, but not reduced to a bare list of outcomes.

---

## 18. Working with Incorrect or Ambiguous Text

If the source text may contain a scientific error:

1. do not hide it through editing;
2. identify the problem;
3. briefly explain why the wording may be incorrect;
4. propose a correction only within the limits of the available information.

If several interpretations are possible, state them explicitly.

Do not shorten ambiguous material in a way that removes the ambiguity instead of resolving or reporting it.

---

## 19. Final Self-Check

Before returning scientific text, verify:

### Scientific Meaning
- Were any unsupported facts added?
- Do all conclusions follow from the available evidence?
- Was the meaning of the source text preserved?
- Were the advantages of the method overstated?
- Were important limitations stated?
- Was important explanatory content removed?

### Claim and Evidence Alignment
- Does every nontrivial claim have a basis?
- Are performance claims scoped by metric, baseline, and operating condition?
- Is novelty supported by literature evidence?
- Are observation and explanation clearly separated?

### Logic and Structure
- Is the problem statement clear?
- Does the method follow from the stated problem?
- Does each paragraph have a dominant function?
- Are supporting explanations present where needed?
- Are logical prerequisites introduced before dependent claims or methods?
- Are there any filler paragraphs or broken transitions?
- Were distinct scientific functions merged excessively?

### Technical Consistency
- Is notation consistent?
- Are central symbols defined before use?
- Do numerical values match?
- Are units consistent?
- Are metrics defined correctly?
- Are text, formulas, tables, and figures aligned?

### Mathematical Exposition
- Are important equations motivated or oriented?
- Are new symbols defined?
- Is the role of each major equation understandable?
- Are derivations and assumptions presented in logical order?
- Was explanatory text around formulas preserved where useful?

### Rewrite Fidelity
When rewriting an existing text:
- Is the rewritten text similar in substantive coverage to the source?
- Was the literature review compressed too aggressively?
- Were methodological explanations removed?
- Were experiment conditions removed?
- Were result interpretations or limitations removed?
- Did rewriting accidentally become summarization?
- Is the length roughly appropriate for the source and task?

### Style
- Does the text follow the required language-specific style references?
- Is there unnecessary filler?
- Is there repetition that can be removed without losing explanation?
- Is there promotional wording?
- Are transitions logically justified?
- Is the text natural rather than mechanically compressed?
- For Russian text, does it comply with `references/style-guide_ru.md`?

### Sources
- Are sources provided where required?
- Were any references fabricated?
- Does each source actually support the corresponding claim?

If a scientific uncertainty or evidence gap is identified, report it separately instead of hiding it inside the revised text.

---

## 20. Core Principle

The quality of scientific writing is determined not by minimum length, but by the precision and completeness of the scientific thought.

Remove filler, repetition, and empty phrasing. Preserve explanation, motivation, methodological detail, and discussion when they are necessary for understanding the work.

When elegant wording, persuasiveness, brevity, or stylistic preference conflicts with scientific correctness or necessary explanatory depth, choose scientific correctness and explanatory depth.
