# Disagreement dossier

Every item where `G2` and `G4` differ by 2 or more points on any dimension, or split on the critical-failure flag. Each entry shows both rationales verbatim, so the cause of the split can be read rather than inferred.

**16 of 40 items** qualify.

---

## CON-02 — Commercial contracts (US - New York)

**Question.** A New York-governed SaaS agreement says that any breach of the confidentiality section triggers a flat payment of $500,000. Is that enforceable?

**Trap.** Saying it is enforceable simply because the parties agreed to it, or applying a pure hindsight 'actual damages' test.

**Answer under test** (`B_terse`):

> Generally enforceable under NY law if it bears a reasonable relationship to anticipated harm. $500k may face scrutiny depending on contract value, but fixed damages clauses aren't per se unenforceable. Courts enforce them if not deemed a penalty for unforeseeable breaches.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The answer gestures at 'reasonable relationship to anticipated harm' but never states the two-prong NY test (difficulty of estimation at formation AND reasonable pre-estimate), never flags that a single flat sum for varying breach severity is especially vulnerable, and never addresses the burden of proof; it also cites no authority at all despite Truck Rent-A-Center being the expected case, so D4 is 0 for missing an expected governing authority entirely (no fabrication, but complete absence where one is clearly expected). The phrase 'fixed damages clauses aren't per se unenforceable' combined with vague hedging without naming the controlling test or the formation-time measurement point risks leaving a reader thinking the clause is likely fine, which is misleading given the trap the gold reference flags.
- `G4`: States the rule only as 'reasonable relationship to anticipated harm' and garbles the second prong into 'a penalty for unforeseeable breaches,' omitting the difficult-to-estimate-at-formation element, the measurement-as-of-contract-formation point, the vulnerability of a single flat sum across breaches of differing severity, and the burden on the challenger; no authority cited where Truck Rent-A-Center and Restatement 356 would be expected. Leads with 'Generally enforceable' and gives no facts-that-would-change-the-answer or next step, though it does not flatly invert the rule since it concedes penalty scrutiny.

---

## CON-06 — Corporate / M&A (US - Delaware)

**Question.** Our target is party to a license that says it may not be assigned, including by operation of law, without consent. The buyer proposes a reverse triangular merger with the target surviving. Does that trigger the anti-assignment clause under Delaware law?

**Trap.** Answering yes on the intuition that any merger is an assignment by operation of law.

**Answer under test** (`B_terse`):

> No. Under Delaware law, a reverse triangular merger where the target survives doesn't trigger anti-assignment language. The license stays with the target entity. Only a forward merger or liquidation extinguishing the target triggers 'by operation of law' language.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 2 | -1 |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The answer states the core rule correctly but presents it as an absolute ('doesn't trigger') without acknowledging that express change-of-control language or an expansive clause can change the result, and cites no authority at all despite Meso Scale Diagnostics and 8 Del. C. 259 being the expected governing sources, which under D4 counts as asserting propositions with no authority where a specific governing provision is expected (score 1) - however since no authority is cited at all rather than fabricated, D4=1 not 0; corrected, critical_failure is set based on missing dispositive caveat rather than fabrication. Missing: Meso Scale Diagnostics case name, 8 Del. C. 259, the change-of-control drafting fix, and the note that other states like California reach different results, leaving only about half the must-include points covered.
- `G4`: Gets the core Meso Scale result right ('a reverse triangular merger where the target survives doesn't trigger anti-assignment language') and avoids the trap, but states it as flatly settled without the crucial caveat that an express change-of-control/merger clause changes the result, and the sweeping 'Only a forward merger or liquidation... triggers' overstates; no citation to Meso Scale or 8 Del. C. 259 where a practitioner would expect them, and no flag that the contract's governing law (e.g., California patent-license cases) could alter the analysis.

---

## CON-07 — Commercial contracts (US - general)

**Question.** What is the practical difference between an indemnity and a duty to defend, and why does it matter which one we negotiate?

**Trap.** Treating the two as synonyms.

**Answer under test** (`A_standard`):

> An indemnity is a passive obligation to compensate the other party for losses incurred; a duty to defend is an active obligation to provide counsel and bear defense costs in real time. The distinction matters significantly. A duty to defend is broader and more valuable—it requires representation during litigation regardless of whether the claim ultimately falls within the indemnity's scope. Indemnitees strongly prefer duty-to-defend language because it shifts legal control to the indemnitor. In negotiation, push for indemnity-only language if representing the indemnitee, or insist on narrow duty-to-defend triggers if representing the indemnitor. This distinction also affects insurance coverage analysis, as policies often carve out duty-to-defend obligations. Precision in the contract language is essential to avoiding disputes with insurers.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 2 | 1 | +1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 2 | 1 | +1 |
| D5 Scope discipline | 1 | 0 | +1 |
| Critical failure | False | True | **SPLIT** |

- `G2`: The answer contains an internal error: it advises indemnitees to prefer duty-to-defend but then instructs 'push for indemnity-only language if representing the indemnitee,' which inverts the correct recommendation and is materially misleading; it also omits the timing difference (defense costs paid as incurred vs. indemnity paid on resolution) and the point that duty to defend must often be expressly stated rather than implied, both must_include items, and gives directive negotiation advice without flagging jurisdictional variation in whether defense duties are implied.
- `G4`: The answer internally contradicts itself and inverts the parties' interests: it says indemnitees 'strongly prefer duty-to-defend language' but then advises 'push for indemnity-only language if representing the indemnitee,' and mischaracterizes the duty to defend as shifting 'legal control to the indemnitor' as a benefit to the indemnitee without addressing control/settlement-consent as the real negotiation point; it also omits the rule that many states require an express duty to defend and that it is not implied from indemnity, omits the timing/as-incurred point, gives no jurisdictional flagging that defense-duty rules are state-specific, cites no authority, and delivers directive negotiation advice ('push for indemnity-only language') that would mislead a non-lawyer reader.

---

## CON-08 — Commercial contracts (England & Wales)

**Question.** Is an English-law agreement enforceable if one side gives no consideration, provided the document is executed as a deed?

**Trap.** Importing the US rule that consideration is always required, or treating 'deed' as a mere formality with no substantive effect.

**Answer under test** (`B_terse`):

> Yes. Under English law, a deed requires no consideration. Execution as a deed creates binding force solely through formality—delivery and intent—without consideration. That's the entire point.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 3 | -1 |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 2 | 1 | +1 |
| Critical failure | True | False | **SPLIT** |

- `G2`: Correctly states the core rule (deed binding without consideration) but omits execution formalities detail beyond 'delivery and intent', omits the 12 vs 6 year limitation point, the US comparison, and cites no authorities at all (LP(MP)A 1989 s.1, CA 2006 s.44, Limitation Act 1980 s.8 all missing), which under D4's rule counts as fabrication-equivalent silence but more precisely is a total absence of expected named authority triggering the D4=0 floor via the missing-dispositive-provision concern; combined with no mention of the 12-year limitation bar (a dispositive point), this trips the critical-failure flag.
- `G4`: The core proposition ('Under English law, a deed requires no consideration') is correct and the trap is avoided, but the answer covers only one of four must-include points — it omits the s.1 LP(MP)A 1989 / s.44 Companies Act 2006 execution formalities (mentioning only 'delivery and intent'), the 12-year limitation period under s.8 Limitation Act 1980, and the divergence from US law — and cites no authority at all where specific governing provisions would be expected. 'That's the entire point' delivers a clean conclusion with no statement of the facts or formalities on which enforceability actually depends.

---

## COR-03 — Corporate / M&A (US - Delaware)

**Question.** Do our client's stockholders have appraisal rights in a cash-out merger of a NYSE-listed Delaware corporation?

**Trap.** Stopping at the market-out exception and concluding there are no appraisal rights in a listed-company cash deal.

**Answer under test** (`A_standard`):

> Under Delaware General Corporation Law § 262, stockholders have appraisal rights in mergers, and these rights generally apply to NYSE-listed corporations. However, Delaware courts have held that if the merger price reflects fair value—as evidenced by arm's-length negotiations, market check processes, or established market valuations—courts will not award appraisal relief exceeding the merger consideration. The availability of appraisal rights exists in theory, but recovery depends on proving the price was below fair value. If the buyer obtained the company at fair value through proper process, appraisal claims provide no relief. The key issue is whether fair value was achieved; if not, appraisal can be valuable.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 0 | 1 | -1 |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 0 | 1 | -1 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The answer never mentions the market-out exception under 262(b)(2) or its exception-to-the-exception for cash-out mergers, instead fabricating a framework about courts denying appraisal above merger price when process was fair — this misstates the actual statutory mechanics entirely and misses the core issue the question presents (whether market-out applies and is then restored by the cash consideration). No statutory sections are cited despite the gold reference expecting 262(b), 262(b)(2), and 262(g), and the answer's substantive claim about courts refusing to award appraisal above deal price absent a bad process is not an accurate statement of Delaware appraisal law, which requires independent fair value determination regardless of process quality in most cases.
- `G4`: The answer never mentions the 262(b)(1) market-out exception or the 262(b)(2) exception-to-the-exception that actually restores appraisal in a cash-out of listed shares, instead asserting generically that '§ 262 ... generally apply to NYSE-listed corporations' — right conclusion by accident, wrong reasoning; it also omits perfection steps (written demand, no vote in favor, continuous holding) and 262(g) de minimis conditions, and pivots entirely to a Dell/DFC-style fair-value merits discussion the question did not ask, citing only '§ 262' generically with no subsection and no case named. Correct Delaware law is invoked but the jurisdiction-specific market-out structure that drives the answer is absent, and the confident 'appraisal claims provide no relief' framing over-asserts on a fact-dependent merits issue.

---

## COR-04 — Corporate / M&A (US - Delaware)

**Question.** Our buyer learned before signing that one of the seller's reps is inaccurate. If the agreement is silent on sandbagging and governed by Delaware law, can the buyer still bring an indemnity claim post-closing?

**Trap.** Stating that pre-closing knowledge always defeats the claim, i.e. inverting the Delaware default.

**Answer under test** (`B_terse`):

> Yes. Delaware law permits sandbagging unless the agreement prohibits it. Pre-signing knowledge of a rep's inaccuracy doesn't bar the indemnity claim—that knowledge relates to the breach itself, not the right to recover.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 2 | +0 |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 2 | 2 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: Correctly states Delaware's pro-sandbagging default and avoids the trap of inverting it, but omits the bargained-for-terms rationale, the point that silence differs from an express anti-sandbagging clause, the NY contrast, and drafting recommendations; no authorities are cited at all despite the gold reference expecting Cobalt Operating and Eagle Force to be named, which triggers D4=0 and the critical-failure flag under the 'no authority where a specific governing case would be expected' standard (treated as failing to cite the expected controlling case law).
- `G4`: The core proposition — 'Delaware law permits sandbagging unless the agreement prohibits it' — is correct and avoids the trap, but it is stated as flatly settled when Delaware's position rests partly on Eagle Force dicta, and the reasoning that pre-signing knowledge 'relates to the breach itself' is imprecise; the answer covers only the first must_include point, omitting the bargained-for-contract-term rationale, the silence-vs-express-anti-sandbagging distinction, the New York contrast, and any drafting response, and cites no authority at all (no Cobalt Operating, Eagle Force, or Ziff-Davis) where a practitioner would expect named cases.

---

## COR-05 — Corporate / tax (US - federal)

**Question.** Our private portfolio company is being acquired and several executives have change-of-control payments. What is the 280G exposure and is there anything we can do about it?

**Trap.** Describing the 3x trigger but omitting that the tax falls on the excess over the base amount, or offering the shareholder vote to a public company.

**Answer under test** (`A_standard`):

> Section 280G imposes a 20% excise tax on executives receiving change-of-control payments exceeding 3x their base compensation plus average annual benefits (the "3x trigger"). The company may also lose tax deductions for excess payments. For private company acquisitions, this is frequently overlooked but can be catastrophic. Mitigation strategies include: (1) obtaining written 280G gross-up waivers from executives, reducing their severance accordingly; (2) restructuring payments to remain below the 3x trigger; (3) timing payments post-closing; or (4) obtaining a fairness opinion supporting the severance as reasonable independent of the change. 280G calculations are complex; engage a specialized valuation firm immediately to assess exposure and model mitigation strategies.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The answer misstates the base amount as 'base compensation plus average annual benefits' (rather than 5-year average W-2 compensation) and, critically, fails to specify that the 20% excise tax and lost deduction apply only to the excess over the base amount, implying the whole payment is taxed — the exact trap flagged in the gold reference; it also entirely omits the private-company shareholder cleansing vote (the single most important private-company mitigation, per must_include), substituting invented/inaccurate mechanisms like '280G gross-up waivers' and 'fairness opinions' that are not recognized 280G mitigation tools, which combined with the missing base-amount clarification constitutes a materially misleading/inverted description of the rule; no statutory citations (280G, 4999, Treas. Reg. 1.280G-1) are given at all, and the invented 'gross-up waiver'/'fairness opinion' mitigation techniques risk being relied upon as if they were established, real practices, tripping the confidently-inverted-rule and fabricated-authority-adjacent concerns even though no case/citation is literally fabricated.
- `G4`: Misstates the mechanics: says the 20% excise tax applies to payments 'exceeding 3x their base compensation' rather than to the excess over the base amount once the 3x threshold is crossed, and misdefines the base amount as 'base compensation plus average annual benefits' instead of the five-year average W-2 compensation; it also mislabels the excise tax as arising under 280G rather than IRC 4999. It omits the single most important private-company remedy — the 280G(b)(5) shareholder cleansing vote (>75% approval with waiver) — and substitutes invented fixes ('280G gross-up waivers,' 'timing payments post-closing,' a 'fairness opinion'), cites no provisions beyond a bare '280G,' and closes with directive 'engage a valuation firm immediately' advice built on the flawed framework.

---

## EMP-01 — Employment (US - federal + state)

**Question.** We have a 'Marketing Manager' paid a $52,000 salary who supervises no one and spends most of her time executing campaigns. Is she exempt from overtime?

**Trap.** Asserting a specific current federal salary threshold as settled, or resolving exempt status from the title alone.

**Answer under test** (`A_standard`):

> Under the Fair Labor Standards Act and most state wage-and-hour laws, exempt status depends on the "duties test," not title or salary alone. A Marketing Manager executing campaigns with no supervisory authority almost certainly fails the "executive" exemption test (requiring management of employees or department). She might qualify for a "creative professional" exemption if her role involves substantial independent creative judgment, but this is fact-specific and rarely applies to campaign execution. At $52,000, salary may exceed current federal thresholds (currently $844/week), but thresholds continue rising. She is almost certainly non-exempt and entitled to overtime compensation. Misclassification exposes the company to back-pay liability, penalties, and attorney fees. Reclassify her immediately and audit similar positions.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 2 | -1 |
| D2 Jurisdictional grounding | 1 | 1 | +0 |
| D3 Issue completeness | 1 | 2 | -1 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The answer asserts a specific current federal salary threshold ('$844/week') as settled fact, which is exactly the trap the gold reference warns against, and this figure is inaccurate/unverifiable given ongoing litigation over the DOL rule; it also fails to mention state-specific thresholds (California, New York) despite the question being flagged as US federal + state, and omits the administrative exemption analysis and the two/three-year FLSA lookback period entirely, while citing no authorities (no 29 U.S.C. 213(a)(1), 29 C.F.R. Part 541, or state wage orders).
- `G4`: Correctly reasons that duties defeat the executive exemption and that title is irrelevant, but asserts '$844/week' as the current federal threshold — a figure that has been enjoined/vacated and is exactly the trap the gold reference flags — and omits the administrative exemption's discretion-and-independent-judgment analysis; it also never mentions state overlays (California/New York higher thresholds) despite the question being framed as federal + state, and cites no authority (no 29 U.S.C. 213(a)(1), no 29 C.F.R. Part 541) while stating the FLSA lookback/liquidated damages only vaguely as 'penalties.'

---

## EMP-04 — Employment (US - federal)

**Question.** An employee has asked to work remotely three days a week as an accommodation. We think the role needs to be on-site. What is our obligation?

**Trap.** Answering that the employer can simply deny because attendance is an essential function, without the interactive process.

**Answer under test** (`B_terse`):

> You must engage in an interactive process. If the role's essential functions genuinely require on-site presence, you can deny it—but you must show why, not assume. If accommodation is feasible, denial risks liability.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 3 | -1 |
| D2 Jurisdictional grounding | 1 | 2 | -1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 2 | 2 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The answer correctly requires the interactive process and rejects a bare denial, avoiding the trap, but omits documentation requests, the effective-alternative rule, undue hardship's employer burden/high bar, and does not flag that state law (e.g. California FEHA) may be broader, so it doesn't address jurisdictional overlay at all (D2 scored 1). No authorities are cited despite the gold reference expecting 42 U.S.C. 12112(b)(5) and 29 C.F.R. 1630.2(o)(3) (D4=0, triggering critical_failure per the hard rule).
- `G4`: The core propositions — 'You must engage in an interactive process' and that denial requires showing the essential functions genuinely require on-site presence rather than assuming — are legally correct and avoid the trap, but the answer omits most must_include points (documentation requests, alternative effective accommodations, undue hardship as the employer's high-bar burden, and broader state law such as California FEHA) and cites no authority where 42 U.S.C. 12112(b)(5) and 29 C.F.R. 1630.2(o)(3) would be expected; it also never flags that state law may impose stricter obligations. Usable as a starting point and correctly hedged ('if... genuinely require'), but too thin to name the facts that would change the answer or give a concrete next step.

---

## EMP-06 — Employment (US - California + federal)

**Question.** We engage software developers in California as 1099 contractors. They use our tools, work our hours, and only work for us. Is that defensible?

**Trap.** Applying only the IRS control test, or blending the ABC and economic-realities tests as if they were one standard.

**Answer under test** (`B_terse`):

> This is likely misclassification. California's ABC test presumes employee status unless: (A) independent schedule, (B) work outside your business, (C) operates independently. These contractors fail all three. Reclassify or face wage-and-hour penalties.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 2 | -1 |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The answer states the ABC test correctly in outline but mischaracterizes prong A as 'independent schedule' rather than freedom from control, and asserts flat conclusion ('fail all three... reclassify') without naming AB 5/Cal. Lab. Code 2775, Dynamex, or Borello, and omits any federal analysis, Borello carve-outs, or specific exposure items like Labor Code 2802/PAGA; no authorities are cited at all, triggering D4=0 and critical_failure, and the confident 'reclassify or face penalties' directive ignores the fact-dependent, multi-test nature the gold reference requires.
- `G4`: Correctly identifies the ABC test and reaches the right bottom line, but paraphrases prong A as 'independent schedule' rather than freedom from control and asserts the contractors 'fail all three' without noting prong B is the decisive failure or that prong C is fact-dependent; no mention of Borello's continuing role, and the federal side of the question (DOL economic-realities / IRS common-law tests, and the possibility of divergent classification) is entirely omitted despite the question naming federal law. Cites no authority at all — no Lab. Code 2775, Dynamex, or 2802 — and gives no exposure detail (overtime, expense reimbursement, PAGA) or concrete next step beyond 'reclassify.'

---

## PRV-02 — Data privacy (US - California)

**Question.** We send hashed emails to an ad platform for audience matching. Is that a 'sale' under the CCPA as amended by the CPRA, and does a service provider contract fix it?

**Trap.** Concluding it is not a sale because no money changed hands, and stopping there.

**Answer under test** (`B_terse`):

> Yes, it's a 'sale' under CPRA—sharing for valuable consideration is a sale even if hashed. Service provider contract doesn't fix this; the ad platform isn't your service provider because it uses the data for its own benefit. Obtain opt-in consent or certified QDE status.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The answer collapses 'sale' and 'share' into one concept ('sharing for valuable consideration is a sale'), missing the crucial CPRA distinction that audience matching is a 'share' regardless of consideration—this is the trap the gold reference specifically warns about, just inverted; it also invents 'certified QDE status' and 'opt-in consent' requirements that are not accurate CCPA/CPRA mechanisms (no such certification/consent regime exists for sale/share, only opt-out), which constitutes fabricated authority triggering critical failure; no statutory citations are given at all (1798.140(ad)/(ah), 1798.100(d)) despite the question calling for them; the answer correctly identifies that the service-provider exception fails because the platform uses data for its own purposes, but omits notice-at-collection, opt-out link, and preference-signal consequences.
- `G4`: Reaches the right bottom line (opt-out obligations attach) but misstates the law by collapsing everything into 'sale' and never mentioning 'share'/cross-context behavioral advertising, which is the operative CPRA concept for audience matching; it also asserts categorically that the platform 'isn't your service provider' without the fact-dependent test (own purposes / combining data) and invents a nonexistent remedy — CCPA requires a 'Do Not Sell or Share' link and opt-out, not 'opt-in consent or certified QDE status.' No statutory citations at all (1798.140(ad)/(ah), 1798.100(d), 1798.120) where a practitioner would expect them; no fabricated case or section is cited, so no critical-failure flag, though 'certified QDE status' is a made-up concept rather than a misattributed authority.

---

## PRV-03 — Health data (US - federal)

**Question.** Our wellness app collects heart-rate and symptom data directly from consumers. Are we a HIPAA business associate?

**Trap.** Concluding that any app handling health information is automatically subject to HIPAA.

**Answer under test** (`A_standard`):

> Generally, no. HIPAA's Business Associate Rule defines a Business Associate as an entity that creates, receives, or transmits Protected Health Information (PHI) AND provides a service to a covered entity. A wellness app selling directly to consumers (not to healthcare providers or insurers) is not a Business Associate under HIPAA. However, this analysis depends on your app's structure: if integrated with healthcare providers or if data is considered PHI by healthcare entities, the analysis changes. Many states impose privacy laws and health-data obligations on consumer apps regardless of HIPAA. Consider compliance with HIPAA as best practice and review applicable state consumer health privacy laws, which often impose stricter requirements than HIPAA.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 2 | +0 |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 2 | 2 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: Correctly concludes no BA relationship and avoids the trap, but D4=0 because the answer names a 'Business Associate Rule' definition without citing 45 C.F.R. 160.103 or any authority, and misstates the test (correct standard is BA acts 'on behalf of' a covered entity, not merely 'provides a service' plus PHI handling); D3 misses FTC Act Section 5, the Health Breach Notification Rule, and specific state statutes (WA My Health My Data Act, NV SB 370) are only vaguely gestured at as 'many states'.
- `G4`: Correctly reaches 'generally, no' and states the BA definition (service to a covered entity), avoiding the trap, but the phrase 'if data is considered PHI by healthcare entities' is imprecise and 'Consider compliance with HIPAA as best practice' is loose advice; it omits the FTC Health Breach Notification Rule, FTC Act Section 5, and named state statutes (My Health My Data Act, Nevada SB 370), and it gestures vaguely at 'many states' without naming any authority such as 45 C.F.R. 160.103 or 16 C.F.R. Part 318.

---

## IPR-04 — Trade secrets (US - federal + California)

**Question.** A senior engineer is leaving for a direct competitor in California. Can we stop him on an inevitable disclosure theory?

**Trap.** Recommending an inevitable-disclosure injunction in California.

**Answer under test** (`B_terse`):

> No. California prohibits non-competes and rejects inevitable disclosure doctrine. You can't enjoin an engineer from working for a competitor unless you prove actual threatened misappropriation—not speculation. California's anti-restraint policy bars this remedy.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 3 | -1 |
| D2 Jurisdictional grounding | 3 | 2 | +1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The core answer (no inevitable disclosure in CA, need actual/threatened misappropriation) is correct and correctly grounded in California law, but no authorities are cited at all despite the gold reference expecting DTSA, CUTSA, Whyte, and PepsiCo (D4=0, triggering critical failure). It omits most of the practical guidance a practitioner would give (reasonable secrecy measures, forensic evidence, DTSA ex parte seizure, risk of attempting to enforce a void non-compete, and that the doctrine is accepted elsewhere like Illinois), and gives a terse conclusory answer without naming next steps or fact-dependencies (D5=1, D3=1).
- `G4`: Correctly states that 'California ... rejects inevitable disclosure doctrine' and requires actual or threatened misappropriation, avoiding the trap, but it names no authority (no Whyte v. Schlage Lock, DTSA or CUTSA) where the gold reference expects specific governing provisions, and omits nearly all the affirmative points — DTSA/CUTSA claims, forensic evidence, reasonable-measures element, ex parte seizure, and the liability risk of attempting to enforce a void non-compete. It also does not flag that the rule is California-specific and accepted elsewhere (PepsiCo line), and gives a flat 'No' with no next step or fact-dependent guidance.

---

## REA-01 — Real estate (US - general)

**Question.** Our commercial lease says landlord consent to assignment will not be unreasonably withheld. Tenant wants to assign to a startup with weaker financials. Can the landlord say no?

**Trap.** Answering that the landlord has absolute discretion, or that consent can never be refused.

**Answer under test** (`A_standard`):

> No, not automatically. A covenant that landlord consent "will not be unreasonably withheld" requires the landlord to exercise judgment reasonably but permits consideration of financial capability, creditworthiness, use suitability, and lease compliance. A startup with weaker financials is a legitimate basis for withholding consent, as the landlord has reasonable concern about non-payment. The tenant must show the landlord's stated reason is pretextual or that refusal was arbitrary or motivated by improper purpose (e.g., extracting higher fees). To challenge the refusal, the tenant needs evidence of improper motivation. Providing financial guarantees, parent-company guarantees, or increased security deposits strengthens the tenant's position. Renegotiating upfront or seeking landlord consent in writing is advisable.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 2 | +0 |
| D2 Jurisdictional grounding | 1 | 1 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G2`: Core reasonableness analysis is correct and correctly treats weaker financials as legitimate, but the answer never flags that states differ on the default rule where the lease is silent (here the lease is not silent, but the answer generalizes 'a covenant requires reasonable judgment' without noting jurisdictional variation on reasonableness standards generally, e.g. Kendall v. Ernest Pestana) and omits deadline/silence-as-consent and post-assignment liability/privity points entirely, so D3 is deficient. No authorities are cited at all despite the gold reference expecting Kendall v. Ernest Pestana and the Restatement, which triggers D4=0 and the critical-failure flag.
- `G4`: Correctly states weaker financials can be a legitimate ground and names improper-purpose/rent-extraction as impermissible, but the burden framing ('tenant must show... pretextual') is stated more firmly than the law supports and the answer omits the contractual response period/deemed-consent point, the state split on the default where the lease is silent, and continuing tenant liability absent an express release; no jurisdictional flagging that reasonableness standards and defaults vary by state, and no citation to Kendall v. Ernest Pestana or the Restatement where a practitioner would expect one.

---

## ETH-01 — Legal ethics / UPL (US - state bar rules)

**Question.** Can a technology company that is not owned by lawyers offer an AI product that answers legal questions for consumers?

**Trap.** Giving a flat yes or no, or treating UPL as a single national standard.

**Answer under test** (`A_standard`):

> This involves complex unauthorized-practice-of-law considerations. Non-lawyers can provide legal information without violating UPL, but cannot provide legal advice, represent clients, or create custom analysis tailored to specific situations. An AI product answering general legal questions may be permissible if it: (1) disclaims it is not legal advice, (2) does not provide situation-specific advice, (3) does not create attorney-client relationships, and (4) does not charge for legal services (which triggers stricter regulation). State bar associations increasingly scrutinize AI legal products. The safest approach: obtain regulatory guidance from relevant state bars, include strong disclaimers, consult counsel in key jurisdictions, and obtain professional liability insurance. The FTC and state AGs may investigate consumer protection issues; proactive compliance is essential.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 2 | +0 |
| D2 Jurisdictional grounding | 1 | 1 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 2 | 2 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G2`: The answer correctly identifies the information-vs-advice line and disclaimers-not-dispositive theme, but treats UPL generically ('state bar associations,' 'relevant state bars') without acknowledging that UPL is defined state-by-state with widely varying standards, and never mentions Arizona's ABS regime or Utah's sandbox as the recognized exceptions, nor cites Model Rules 5.4/5.5 despite discussing their substance (fee-sharing/charging for legal services, attorney-client relationship) - this is an unsupported-authority gap (D4=0) triggering critical failure; D3 misses several must-include points (state-specific variation, ABS/sandbox exceptions, enforcement history against self-help software) leaving only about half covered.
- `G4`: Core information/advice distinction is stated correctly and the answer avoids a flat yes/no, but it presents UPL as a generic national standard ('Non-lawyers can provide legal information without violating UPL') and never says UPL is defined by state law with widely varying definitions; it omits Model Rules 5.4/5.5, the Arizona ABS and Utah sandbox exceptions, and the self-help software enforcement history, and cites no authority at all despite specific governing rules the practitioner would expect. The claim that not charging avoids stricter regulation is also imprecise; D5 is acceptable since it gives concrete next steps but does not name the facts that would change the analysis.

---

## ETH-02 — Legal ethics / confidentiality (US - state bar rules)

**Question.** May a lawyer put confidential client documents into a third-party generative AI tool?

**Trap.** Answering with a flat prohibition, or a flat permission with no consent or verification analysis.

**Answer under test** (`B_terse`):

> Prohibited without informed consent. Uploading to third-party AI risks disclosure and violates duty of confidentiality under Model Rule 1.6. Client must consent recognizing risks. Use lawyer-only AI services or in-house systems.

| Dimension | `G2` | `G4` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 2 | 1 | +1 |
| D3 Issue completeness | 0 | 1 | -1 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | False | True | **SPLIT** |

- `G2`: The answer states 'Prohibited without informed consent' as a near-flat rule, falling into the trap the gold reference explicitly warns against, and omits verification of outputs, ABA Formal Opinion 512, Rule 5.1/5.3 supervision, Rule 1.5 billing, Rule 3.3 candour, and the lack of uniformity across state bars; it cites only Rule 1.6 with no specificity and no discussion of self-learning tools or terms-of-service analysis, giving a directive conclusion without naming the facts (training use, provider access) that would change the answer.
- `G4`: "Prohibited without informed consent" states a categorical rule that ABA Formal Op. 512 does not adopt — consent turns on the tool's terms (training use, provider access, self-learning), so presenting it as settled and universal is a confidently inverted/overstated rule and squarely the gold trap; it cites only Rule 1.6 generically with no Op. 512, no Rule 1.1 cmt. 8 competence duty, no 5.1/5.3 supervision, no 1.5 billing, no 3.3 candour or output-verification/fabricated-citation sanctions, and no acknowledgment that state bar opinions (CA, FL, NY) diverge.

