# Disagreement dossier

Every item where `G1` and `G3` differ by 2 or more points on any dimension, or split on the critical-failure flag. Each entry shows both rationales verbatim, so the cause of the split can be read rather than inferred.

**17 of 40 items** qualify.

---

## CON-03 — Commercial contracts (US - multi-state)

**Question.** Our MSA has a mutual limitation of liability capped at 12 months of fees. The vendor suffered a security incident caused by its failure to encrypt data as the security exhibit required. Does the cap limit our recovery?

**Trap.** Giving a flat yes or no without conditioning on carve-outs.

**Answer under test** (`A_standard`):

> This presents a significant issue. Generally, limitation of liability clauses apply to breach of contract claims, but courts may carve out exceptions when the breach involves egregious conduct, fraud, or violation of a specific contractual safety requirement central to the agreement. Given the vendor's failure to meet an express encryption obligation in the security exhibit, you have a strong argument that the cap is inapplicable. Many courts hold that fundamental breaches of core contractual duties (here, data security) fall outside limitation clauses. Additionally, you should argue gross negligence or willful misconduct exceptions if available in your jurisdiction. The vendor's failure to encrypt, when contractually required, goes to the heart of the security obligation and should not be shielded by a general liability cap.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 3 | -2 **<-** |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 3 | -2 **<-** |
| D4 Authority hygiene | 1 | 2 | -1 |
| D5 Scope discipline | 1 | 3 | -2 **<-** |
| Critical failure | True | False | **SPLIT** |

- `G1`: Advises that the cap is likely inapplicable without once saying to read the carve-outs, and rests on 'fundamental breach of a core duty defeats the cap', which US courts generally do not accept.
- `G3`: Correctly analyzes that breach of express security obligation may fall outside general liability cap; addresses gross negligence exception and core-duty carve-out; good analytical framework.

---

## CON-05 — Commercial contracts (US - New York)

**Question.** Our force majeure clause lists 'acts of God, war, terrorism, and government orders' but does not mention epidemics or pandemics. A state health order shut our client's venue. Can they invoke force majeure under New York law?

**Trap.** Assuming a pandemic is automatically covered, or reciting the more permissive approach of other jurisdictions as New York law.

**Answer under test** (`A_standard`):

> Under New York law, force majeure clauses are construed narrowly and typically excuse performance only for events specifically listed or clearly contemplated. Since your clause lists "acts of God, war, terrorism, and government orders" but omits pandemics, a court would likely hold it inapplicable to the health order closure. While "acts of God" sometimes receives broad interpretation, New York courts limit this to truly unforeseeable natural events, and COVID-related closures are now foreseeable. You might argue the health order qualifies as a "government order," but this argument is weak given the clause's specific enumeration. The preferable approach is seeking contractual amendment or reformation with the counterparty rather than litigating force majeure applicability.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 3 | -2 **<-** |
| D2 Jurisdictional grounding | 3 | 3 | +0 |
| D3 Issue completeness | 1 | 3 | -2 **<-** |
| D4 Authority hygiene | 1 | 2 | -1 |
| D5 Scope discipline | 1 | 3 | -2 **<-** |
| Critical failure | False | False | - |

- `G1`: Narrow-construction rule stated correctly, then calls the 'government orders' argument weak because of the specific enumeration - government orders is in the enumeration and is the strongest hook. No Kel Kim, no impossibility or frustration alternatives.
- `G3`: Correctly applies New York narrow construction of force majeure, identifies government order as the strongest argument, and discusses alternatives; solid analysis with practical next step.

---

## CON-07 — Commercial contracts (US - general)

**Question.** What is the practical difference between an indemnity and a duty to defend, and why does it matter which one we negotiate?

**Trap.** Treating the two as synonyms.

**Answer under test** (`A_standard`):

> An indemnity is a passive obligation to compensate the other party for losses incurred; a duty to defend is an active obligation to provide counsel and bear defense costs in real time. The distinction matters significantly. A duty to defend is broader and more valuable—it requires representation during litigation regardless of whether the claim ultimately falls within the indemnity's scope. Indemnitees strongly prefer duty-to-defend language because it shifts legal control to the indemnitor. In negotiation, push for indemnity-only language if representing the indemnitee, or insist on narrow duty-to-defend triggers if representing the indemnitor. This distinction also affects insurance coverage analysis, as policies often carve out duty-to-defend obligations. Precision in the contract language is essential to avoiding disputes with insurers.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 3 | -2 **<-** |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 2 | 2 | +0 |
| D4 Authority hygiene | 3 | 2 | +1 |
| D5 Scope discipline | 1 | 3 | -2 **<-** |
| Critical failure | False | False | - |

- `G1`: Distinguishes the two obligations correctly, then reverses the negotiation advice - says the duty to defend is more valuable to the indemnitee and in the next line tells the indemnitee to push for indemnity-only. No citation expected here.
- `G3`: Correctly distinguishes the two duties and their timing/control implications; omits that express statement of duty to defend is required by law in many jurisdictions.

---

## COR-01 — Corporate / M&A (US - Delaware)

**Question.** What stockholder approval is required for a Delaware corporation to merge, and is there a way to close a public deal without a stockholder meeting?

**Trap.** Stating only the 251 majority-of-outstanding rule and omitting the 251(h) route, or describing a majority of votes cast rather than outstanding.

**Answer under test** (`A_standard`):

> Under Delaware General Corporation Law § 251, a merger requires stockholder approval by each constituent corporation. However, Delaware permits a "short-form merger" under § 253 when a parent owns 90% or more of the subsidiary's stock—no vote is required. For an all-cash public deal, stockholder approval is essentially mandatory unless the parties already qualify for short-form merger status. Some deals use written consents in lieu of a stockholder meeting, but public companies face significant SEC compliance issues with this approach. The practical reality is that publicly-traded companies must hold a stockholder meeting or use a time-consuming written consent process. Alternative structures (e.g., triangular mergers) offer no circumvention of this requirement for public companies.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 3 | -2 **<-** |
| D2 Jurisdictional grounding | 3 | 3 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 2 | 2 | +0 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G1`: Asserts that a public company must hold a stockholder meeting and that no structure avoids it - DGCL 251(h) is exactly that structure and is never mentioned. Sections 251 and 253 cited correctly.
- `G3`: Fails to address DGCL 251(h) tender-offer merger route, which is the primary mechanism for closing public deals without stockholder vote; major omission for this question.

---

## COR-03 — Corporate / M&A (US - Delaware)

**Question.** Do our client's stockholders have appraisal rights in a cash-out merger of a NYSE-listed Delaware corporation?

**Trap.** Stopping at the market-out exception and concluding there are no appraisal rights in a listed-company cash deal.

**Answer under test** (`A_standard`):

> Under Delaware General Corporation Law § 262, stockholders have appraisal rights in mergers, and these rights generally apply to NYSE-listed corporations. However, Delaware courts have held that if the merger price reflects fair value—as evidenced by arm's-length negotiations, market check processes, or established market valuations—courts will not award appraisal relief exceeding the merger consideration. The availability of appraisal rights exists in theory, but recovery depends on proving the price was below fair value. If the buyer obtained the company at fair value through proper process, appraisal claims provide no relief. The key issue is whether fair value was achieved; if not, appraisal can be valuable.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 3 | 3 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 2 | 0 | +2 **<-** |
| D5 Scope discipline | 2 | 2 | +0 |
| Critical failure | False | True | **SPLIT** |

- `G1`: Never mentions the market-out exception or the exception to it, which is the whole question; pivots to a fair-value discussion. Section 262 cited correctly but no subsections or perfection steps.
- `G3`: Fails to identify that cash-out mergers restore DGCL 262 appraisal rights despite market-out exception; incorrectly frames recovery as dependent on fair-value process when statute provides unconditional appraisal availability.

---

## COR-06 — Antitrust / M&A (US - federal)

**Question.** Does our $110 million acquisition require an HSR filing?

**Trap.** Asserting a specific current dollar threshold as settled fact without flagging that it changes annually.

**Answer under test** (`B_terse`):

> No. The HSR threshold is $111.4 million (2024). At $110 million, the deal is below threshold. No HSR filing required unless this involves partial interest aggregation or foreign commerce complications.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G1`: States a specific dollar threshold as current law and concludes no filing is required on that basis, with no mention that HSR thresholds are adjusted annually. That is a reportable-transaction risk, not a rounding error.
- `G3`: Violates rubric guidance by asserting specific 2024 threshold ($111.4M) as settled law without acknowledging annual adjustment; should direct to FTC notice rather than fix threshold.

---

## EMP-05 — Employment (US - federal + California)

**Question.** We are closing a California site and laying off 62 people out of a 240-person company. Do we need to give notice?

**Trap.** Answering under federal WARN only and concluding no notice is required.

**Answer under test** (`A_standard`):

> Yes. California requires compliance with both the federal WARN Act and California's CIPA (California Integrated Plant Closure Act). Both require 60 days' written notice for mass layoffs affecting 50 or more employees at a single site. Your client is laying off 62 out of 240 employees, triggering both requirements. Failure to provide notice results in penalties of up to 60 days' backpay and benefits for each affected employee, plus potential attorney fees. Additionally, California requires final paychecks on the last day of employment, including all earned wages and accrued paid-time-off. Provide written notice immediately and ensure compliance with final pay requirements. This is a critical compliance issue with significant liability exposure.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 3 | -2 **<-** |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 2 | 2 | +0 |
| D4 Authority hygiene | 0 | 2 | -2 **<-** |
| D5 Scope discipline | 2 | 3 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G1`: Right conclusion (notice required) but invents 'California Integrated Plant Closure Act (CIPA)' - Cal-WARN is Lab. Code 1400 et seq.; also misstates the federal trigger as a flat 50 at a single site.
- `G3`: Correctly applies both federal and California notice requirements but conflates the 60-day federal timeline with state requirements and mixes in final-paycheck rule which is separate CA wage law.

---

## LIT-02 — Litigation procedure (US - federal)

**Question.** We already filed our answer but want to attack the complaint's sufficiency. What is our vehicle and what standard applies?

**Trap.** Advising that a 12(b)(6) motion can still be filed after the answer, or that the argument is waived.

**Answer under test** (`B_terse`):

> Motion to dismiss under Rule 12(e) for failure to state a claim (if not earlier raised, waived) or motion for judgment on pleadings under Rule 12(c). Standard: complaint must plead facts raising plausible inference of liability.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 2 | -1 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G1`: Cites 'Rule 12(e)' for failure to state a claim - that is the motion for a more definite statement. Also says the defence is waived if not earlier raised, contrary to Rule 12(h)(2). Correctly names 12(c).
- `G3`: Misstates vehicle as Rule 12(e) when correct answer is Rule 12(c); omits that failure to state is preserved under 12(h)(2); minimal discussion of Twombly/Iqbal plausibility standard.

---

## LIT-03 — Litigation procedure (US - federal / constitutional)

**Question.** Our client is sued in Montana over a product it sold nationwide but not specifically into Montana; the particular unit was resold there by a third party. Can the court exercise specific personal jurisdiction?

**Trap.** Applying a but-for causation requirement and concluding there is no jurisdiction because the defendant did not sell that unit into the forum.

**Answer under test** (`A_standard`):

> This implicates specific personal jurisdiction under International Shoe Co. v. Washington. A court may exercise specific jurisdiction if: (1) the defendant has a substantial connection to the forum, (2) the claim arises from that connection, and (3) exercise is reasonable. Your client's position is weak: it sold nationwide but not to Montana; the unit reached Montana through third-party resale. Most courts hold this insufficient for specific jurisdiction because your client did not "purposefully avail" itself of Montana by directing sales there. The resale is a superseding act. Absent evidence that your client knew the product would reach Montana or directed it there, specific jurisdiction likely fails. General jurisdiction also fails absent physical presence in Montana. This is a solid motion-to-dismiss argument.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 0 | 2 | -2 **<-** |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 0 | 1 | -1 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G1`: Applies a but-for purposeful-availment test and concludes no jurisdiction on facts that are essentially Ford v. Montana; never mentions 'relates to'. Also misstates general jurisdiction as requiring physical presence.
- `G3`: Fails to cite or apply Ford Motor v. Montana (2021), which permits jurisdiction where defendant systematically served the same market nationwide; analysis is overly pessimistic and misses the relates-to prong.

---

## LIT-04 — Litigation procedure (US - federal)

**Question.** We were served with a state-court complaint 40 days ago. Diversity is complete, the amount exceeds $75,000, and one co-defendant is a citizen of the forum state. Can we remove?

**Trap.** Overlooking either the expired 30-day clock or the forum-defendant rule, and answering yes.

**Answer under test** (`B_terse`):

> No. Diversity is incomplete—one co-defendant is a forum state citizen. Removal requires complete diversity (all defendants different from all plaintiffs). Motion to remand will succeed.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 0 | 3 | -3 **<-** |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 0 | 2 | -2 **<-** |
| D4 Authority hygiene | 1 | 0 | +1 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G1`: Says diversity is incomplete because a co-defendant is a forum citizen - that conflates the forum-defendant rule with complete diversity, and contradicts the stated facts. Misses the expired 30-day removal window entirely.
- `G3`: Correctly concludes removal barred but provides minimal explanation; fails to cite 28 U.S.C. 1441(b)(2) forum-defendant rule or discuss the 30-day removal window under 1446(b).

---

## LIT-05 — Litigation / e-discovery (US - federal)

**Question.** Our client's auto-delete policy wiped a custodian's mailbox four months after the demand letter arrived. What sanctions are we exposed to?

**Trap.** Stating that an adverse-inference instruction is available on a showing of negligence.

**Answer under test** (`A_standard`):

> This presents serious sanctions exposure under Fed. R. Civ. P. 37 and the court's inherent powers. An auto-delete policy destroying relevant documents after a demand letter is received constitutes spoliation or destruction of evidence, even if the policy predated the dispute. Courts typically impose sanctions ranging from adverse inference instructions (jury told destroyed evidence is deemed unfavorable to the destroyer) to default judgment. The key factor is whether destruction was done in bad faith or was merely negligent; destroying emails four months after demand is likely viewed as intentional or reckless. Possible sanctions include: adverse inferences, preclusion of evidence, attorney fees, default, or case dismissal. Consult litigation counsel immediately. Prospectively, suspend auto-delete policies and issue a litigation hold.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 2 | -1 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 3 | -2 **<-** |
| D4 Authority hygiene | 1 | 2 | -1 |
| D5 Scope discipline | 2 | 3 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G1`: Frames the standard as bad faith versus negligence and offers an adverse inference on a recklessness finding; Rule 37(e)(2) requires intent to deprive. Invokes inherent powers, which 37(e) displaced for ESI.
- `G3`: Correctly applies Rule 37(e) framework but slightly conflates the Intent requirement for adverse inferences with the fact-pattern; covers most key points and appropriate remedies.

---

## LIT-06 — Privilege (US - federal)

**Question.** Our in-house counsel interviewed twelve employees about a compliance issue and sent a summary memo to the CFO. Is all of it privileged?

**Trap.** Asserting blanket privilege over the entire investigation including the underlying facts.

**Answer under test** (`B_terse`):

> Not all. Interview summaries and factual employee statements lack privilege. Only the attorney's legal advice and work product in the memo are protected. Factual portions and statements are discoverable.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 0 | 3 | -3 **<-** |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 2 | -1 |
| D4 Authority hygiene | 1 | 0 | +1 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G1`: Says interview summaries and employee statements lack privilege. Upjohn protects those communications; it is the underlying facts that are not privileged. Acting on this would produce privileged material.
- `G3`: Correctly distinguishes privileged advice from discoverable facts but fails to cite Upjohn, omits work-product analysis, and does not mention Upjohn warnings or waiver risk.

---

## PRV-02 — Data privacy (US - California)

**Question.** We send hashed emails to an ad platform for audience matching. Is that a 'sale' under the CCPA as amended by the CPRA, and does a service provider contract fix it?

**Trap.** Concluding it is not a sale because no money changed hands, and stopping there.

**Answer under test** (`B_terse`):

> Yes, it's a 'sale' under CPRA—sharing for valuable consideration is a sale even if hashed. Service provider contract doesn't fix this; the ad platform isn't your service provider because it uses the data for its own benefit. Obtain opt-in consent or certified QDE status.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 3 | -2 **<-** |
| D2 Jurisdictional grounding | 3 | 3 | +0 |
| D3 Issue completeness | 2 | 2 | +0 |
| D4 Authority hygiene | 0 | 1 | -1 |
| D5 Scope discipline | 2 | 3 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G1`: Gets the substance right - it is covered and the service-provider exception fails - but prescribes 'opt-in consent or certified QDE status', which is not a CCPA mechanism. CCPA is an opt-out regime for adults.
- `G3`: Correctly identifies as CPRA sale and service-provider exception failure but omits statutory notice/link obligations and does not cite CPRA sections.

---

## PRV-04 — Data privacy (EU + US - multi)

**Question.** We confirmed a breach affecting users in Germany, California and Texas. What are our notification deadlines?

**Trap.** Applying the GDPR 72-hour deadline to the US state notifications.

**Answer under test** (`B_terse`):

> Germany (GDPR): 72 hours to regulators. California: without unreasonable delay (typically 30 days). Texas: without unreasonable delay. Comply with GDPR's strictest 72-hour timeline for all jurisdictions simultaneously.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 1 | +1 |
| D2 Jurisdictional grounding | 2 | 1 | +1 |
| D3 Issue completeness | 2 | 1 | +1 |
| D4 Authority hygiene | 1 | 0 | +1 |
| D5 Scope discipline | 2 | 2 | +0 |
| Critical failure | False | True | **SPLIT** |

- `G1`: Separates the three regimes correctly, then tells the client to apply the 72-hour GDPR clock everywhere, which collapses the distinction the question is testing. The '30 days' gloss on California is not in the statute.
- `G3`: Violates critical distinction between GDPR 72-hour rule (EU only) and US state rules; implies applying GDPR deadline to California and Texas, which are separate regimes; major jurisdictional error.

---

## PRV-05 — AI regulation (EU)

**Question.** We sell an AI legal-research assistant to law firms in the EU. How does the EU AI Act classify it and what do we have to do?

**Trap.** Asserting a single blanket compliance date, or classifying it as high-risk without reference to Annex III.

**Answer under test** (`A_standard`):

> Under the EU AI Act, an AI legal-research assistant is likely classified as "high-risk" (Annex III, Category 8: AI for law enforcement and justice). If the tool is primarily informational and does not make binding legal determinations, it may be classified lower. High-risk AI requires: (1) conformity assessments, (2) quality management systems, (3) training-data documentation, (4) human oversight, (5) audit logs, and (6) notified body review. Additionally, you must provide transparency disclosures that output is AI-generated. Law firms have professional responsibilities for legal advice, potentially creating hesitation to adopt unregulated AI tools. The safest approach: obtain regulatory guidance from EU counsel, mark outputs as AI-generated, and secure professional liability insurance. The AI Act's enforcement deadline is approaching; compliance is now urgent.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 3 | -2 **<-** |
| D2 Jurisdictional grounding | 3 | 3 | +0 |
| D3 Issue completeness | 1 | 2 | -1 |
| D4 Authority hygiene | 2 | 2 | +0 |
| D5 Scope discipline | 2 | 3 | -1 |
| Critical failure | False | False | - |

- `G1`: Classifies a tool sold to private firms as Annex III high risk and labels point 8 as law enforcement; also asserts notified-body review and a single approaching deadline. No GPAI obligations and no provider/deployer distinction.
- `G3`: Correctly identifies Annex III Category 8 high-risk classification analysis but does not clearly explain that informational tools for private law firms may not qualify; omits GPAI provider obligations and provider-vs-deployer distinction.

---

## IPR-01 — Intellectual property (US - federal)

**Question.** We hired a freelance designer to create our logo and the invoice says 'work made for hire.' Do we own the copyright?

**Trap.** Answering yes because the document says 'work made for hire.'

**Answer under test** (`A_standard`):

> Not necessarily. Although the invoice references "work made for hire," this language alone is insufficient under U.S. copyright law. A "work made for hire" requires either: (1) a written agreement signed by the creator before or at the time of creation, OR (2) work falling within specific categories (e.g., employee works in scope of employment). An invoice signed after creation is typically ineffective to establish work-made-for-hire status. The correct approach is a separate written copyright assignment. To secure ownership, obtain a written work-made-for-hire agreement or copyright assignment before the designer begins work. If the current document is insufficient, consider a retroactive written assignment. Without proper documentation, you may hold only a license, not ownership of the copyright.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 3 | -2 **<-** |
| D2 Jurisdictional grounding | 2 | 2 | +0 |
| D3 Issue completeness | 2 | 2 | +0 |
| D4 Authority hygiene | 1 | 3 | -2 **<-** |
| D5 Scope discipline | 3 | 3 | +0 |
| Critical failure | False | False | - |

- `G1`: Right conclusion and the right fix (written assignment), but states the nine categories and a signed writing as alternatives when they are cumulative for a contractor, and blends in the employee route. No statute cited.
- `G3`: Correctly identifies WMFH failure and assignment solution but omits California employment consequences under Labor Code 3351.5 and trademark-rights distinction.

---

## REA-02 — Real estate / finance (US - general)

**Question.** The lender is asking for both an estoppel certificate and an SNDA from our tenant. Are these the same thing?

**Trap.** Treating the two documents as equivalent.

**Answer under test** (`B_terse`):

> No. An estoppel certificate certifies lease terms, rent paid, and no defaults. An SNDA (subordination, non-disturbance, attornment) subordinates the lease to the lender's mortgage and protects the tenant if the lender forecloses. Different documents, different purposes.

| Dimension | `G1` | `G3` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 3 | 3 | +0 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 2 | 2 | +0 |
| D4 Authority hygiene | 3 | 1 | +2 **<-** |
| D5 Scope discipline | 2 | 3 | -1 |
| Critical failure | False | False | - |

- `G1`: Correctly distinguishes the two instruments and identifies non-disturbance as the foreclosure protection. Jurisdiction barely engaged, scored 2 per adjudication rule 3. No negotiation points or delivery deadlines.
- `G3`: Correctly distinguishes the two documents and their different functions but omits tenant negotiation points on non-disturbance terms and successor-landlord carve-outs.

