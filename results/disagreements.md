# Disagreement dossier

Every item where `G4` and `G5` differ by 2 or more points on any dimension, or split on the critical-failure flag. Each entry shows both rationales verbatim, so the cause of the split can be read rather than inferred.

**13 of 40 items** qualify.

---

## CON-01 — Commercial contracts (UCC) (US - UCC Art. 2 (general))

**Question.** Our client (a merchant) sent a purchase order for 10,000 units. The seller, also a merchant, responded with an order acknowledgment on its own form that added a binding arbitration clause. Nobody objected; the goods shipped and were accepted. Is the arbitration clause part of the contract?

**Trap.** Answering with a confident yes or no, or applying the common-law mirror-image / last-shot rule.

**Answer under test** (`A_standard`):

> Under UCC Article 2's "battle of the forms" provision (§ 2-207), when both parties are merchants, additional terms in an acceptance may become part of the contract unless they materially alter the deal. An arbitration clause is generally deemed a material alteration. However, given that goods were shipped and accepted without documented objection to the clause, a court may find the arbitration clause binding through course of performance and course of dealing. Most courts hold that silence plus acceptance evidences implied assent. The critical factors are: whether the buyer had reasonable notice of the clause, whether there was any manifestation of rejection, and the jurisdiction's interpretation of materiality. Your strongest argument is that acceptance of goods despite notice of the clause constitutes assent to its inclusion in the contract.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 1 | 2 | -1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 3 | -2 **<-** |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | True | True | - |

- `G4`: The answer states as settled that "[a]n arbitration clause is generally deemed a material alteration" and then contradicts that by asserting "[m]ost courts hold that silence plus acceptance evidences implied assent" — an unsupported, effectively last-shot/implied-assent proposition that inverts 2-207(2)'s rule that materially altering terms drop out absent assent, and the answer never mentions 2-207(2)(b)'s three exceptions or 2-207(3)'s knockout/gap-filler path; it cites only § 2-207 generically while attributing a 'most courts' holding to no authority, and it steers the client toward a conclusion on a point the gold reference marks as genuinely split.
- `G5`: The statement that 'Most courts hold that silence plus acceptance evidences implied assent' confidently reverses the protection against incorporation of materially altering terms, and the recommended 'strongest argument' rests on that error. The answer cites the real, applicable § 2-207 and acknowledges jurisdictional variation, but does not explain the genuine arbitration-materiality split, omits the offer-limitation exception and § 2-207(3), and treats non-objection and acceptance as stronger grounds for incorporation than it can support.

---

## CON-05 — Commercial contracts (US - New York)

**Question.** Our force majeure clause lists 'acts of God, war, terrorism, and government orders' but does not mention epidemics or pandemics. A state health order shut our client's venue. Can they invoke force majeure under New York law?

**Trap.** Assuming a pandemic is automatically covered, or reciting the more permissive approach of other jurisdictions as New York law.

**Answer under test** (`A_standard`):

> Under New York law, force majeure clauses are construed narrowly and typically excuse performance only for events specifically listed or clearly contemplated. Since your clause lists "acts of God, war, terrorism, and government orders" but omits pandemics, a court would likely hold it inapplicable to the health order closure. While "acts of God" sometimes receives broad interpretation, New York courts limit this to truly unforeseeable natural events, and COVID-related closures are now foreseeable. You might argue the health order qualifies as a "government order," but this argument is weak given the clause's specific enumeration. The preferable approach is seeking contractual amendment or reformation with the counterparty rather than litigating force majeure applicability.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G4`: The answer inverts the strongest argument: it calls the 'government order' hook 'weak given the clause's specific enumeration' when in fact the state health order is an enumerated event and is the operative trigger under New York's narrow-construction rule (Kel Kim), and it asserts without support that foreseeability of COVID defeats the clause; it omits ejusdem generis, causation/prevention-not-mere-unprofitability, and the impossibility/frustration alternatives, cites no authority at all, and pushes the client toward renegotiation rather than the available contractual argument.
- `G5`: The answer identifies New York's narrow construction rule, but calling the expressly enumerated 'government order' argument 'weak given the clause's specific enumeration' materially misapplies that rule and substitutes present-day COVID foreseeability for analysis of the actual shutdown. It omits causation/prevention, ejusdem generis, and the narrow impossibility/frustration alternatives, cites no Kel Kim authority, and recommends amendment or reformation without examining the contractual language or performance affected.

---

## CON-07 — Commercial contracts (US - general)

**Question.** What is the practical difference between an indemnity and a duty to defend, and why does it matter which one we negotiate?

**Trap.** Treating the two as synonyms.

**Answer under test** (`A_standard`):

> An indemnity is a passive obligation to compensate the other party for losses incurred; a duty to defend is an active obligation to provide counsel and bear defense costs in real time. The distinction matters significantly. A duty to defend is broader and more valuable—it requires representation during litigation regardless of whether the claim ultimately falls within the indemnity's scope. Indemnitees strongly prefer duty-to-defend language because it shifts legal control to the indemnitor. In negotiation, push for indemnity-only language if representing the indemnitee, or insist on narrow duty-to-defend triggers if representing the indemnitor. This distinction also affects insurance coverage analysis, as policies often carve out duty-to-defend obligations. Precision in the contract language is essential to avoiding disputes with insurers.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 1 | 2 | -1 |
| D3 Issue completeness | 1 | 2 | -1 |
| D4 Authority hygiene | 1 | 2 | -1 |
| D5 Scope discipline | 0 | 0 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G4`: The answer internally contradicts itself and inverts the parties' interests: it says indemnitees 'strongly prefer duty-to-defend language' but then advises 'push for indemnity-only language if representing the indemnitee,' and mischaracterizes the duty to defend as shifting 'legal control to the indemnitor' as a benefit to the indemnitee without addressing control/settlement-consent as the real negotiation point; it also omits the rule that many states require an express duty to defend and that it is not implied from indemnity, omits the timing/as-incurred point, gives no jurisdictional flagging that defense-duty rules are state-specific, cites no authority, and delivers directive negotiation advice ('push for indemnity-only language') that would mislead a non-lawyer reader.
- `G5`: The answer correctly distinguishes compensation from defense costs paid 'in real time,' but overstates defense obligations and insurance exclusions, omits settlement-consent rights and state-specific express-defense requirements, and misleadingly directs an indemnitee to 'push for indemnity-only language' without establishing its objectives. Its general US framing lacks needed state-law qualifications; authority hygiene is barely engaged because no authorities are cited and the gold identifies drafting practice rather than a specific governing provision.

---

## COR-01 — Corporate / M&A (US - Delaware)

**Question.** What stockholder approval is required for a Delaware corporation to merge, and is there a way to close a public deal without a stockholder meeting?

**Trap.** Stating only the 251 majority-of-outstanding rule and omitting the 251(h) route, or describing a majority of votes cast rather than outstanding.

**Answer under test** (`A_standard`):

> Under Delaware General Corporation Law § 251, a merger requires stockholder approval by each constituent corporation. However, Delaware permits a "short-form merger" under § 253 when a parent owns 90% or more of the subsidiary's stock—no vote is required. For an all-cash public deal, stockholder approval is essentially mandatory unless the parties already qualify for short-form merger status. Some deals use written consents in lieu of a stockholder meeting, but public companies face significant SEC compliance issues with this approach. The practical reality is that publicly-traded companies must hold a stockholder meeting or use a time-consuming written consent process. Alternative structures (e.g., triangular mergers) offer no circumvention of this requirement for public companies.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 0 | 0 | +0 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 0 | 1 | -1 |
| D4 Authority hygiene | 1 | 3 | -2 **<-** |
| D5 Scope discipline | 0 | 1 | -1 |
| Critical failure | True | True | - |

- `G4`: The answer states that for a public deal "stockholder approval is essentially mandatory unless the parties already qualify for short-form merger status" and that "publicly-traded companies must hold a stockholder meeting or use a time-consuming written consent process" — this is the inverted rule the gold trap names, since DGCL 251(h) permits closing after a qualifying any-and-all tender offer with no separate vote; it also never states the majority-of-outstanding-shares standard, omits charter/class-vote overlays, and cites only 251 and 253 without the governing 251(h) provision, while giving directive practical advice that would mislead a reader.
- `G5`: The statement that public companies 'must hold a stockholder meeting or use a time-consuming written consent process' confidently contradicts DGCL § 251(h), triggering a critical failure; the answer also omits board approval, the majority-of-outstanding threshold, charter or contractual voting requirements, and § 251(h)'s conditions. It applies Delaware law and cites real, relevant §§ 251 and 253, but its categorical practical conclusion is unsupported and excludes the principal public-deal alternative.

---

## COR-03 — Corporate / M&A (US - Delaware)

**Question.** Do our client's stockholders have appraisal rights in a cash-out merger of a NYSE-listed Delaware corporation?

**Trap.** Stopping at the market-out exception and concluding there are no appraisal rights in a listed-company cash deal.

**Answer under test** (`A_standard`):

> Under Delaware General Corporation Law § 262, stockholders have appraisal rights in mergers, and these rights generally apply to NYSE-listed corporations. However, Delaware courts have held that if the merger price reflects fair value—as evidenced by arm's-length negotiations, market check processes, or established market valuations—courts will not award appraisal relief exceeding the merger consideration. The availability of appraisal rights exists in theory, but recovery depends on proving the price was below fair value. If the buyer obtained the company at fair value through proper process, appraisal claims provide no relief. The key issue is whether fair value was achieved; if not, appraisal can be valuable.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 2 | -1 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | False | True | **SPLIT** |

- `G4`: The answer never mentions the 262(b)(1) market-out exception or the 262(b)(2) exception-to-the-exception that actually restores appraisal in a cash-out of listed shares, instead asserting generically that '§ 262 ... generally apply to NYSE-listed corporations' — right conclusion by accident, wrong reasoning; it also omits perfection steps (written demand, no vote in favor, continuous holding) and 262(g) de minimis conditions, and pivots entirely to a Dell/DFC-style fair-value merits discussion the question did not ask, citing only '§ 262' generically with no subsection and no case named. Correct Delaware law is invoked but the jurisdiction-specific market-out structure that drives the answer is absent, and the confident 'appraisal claims provide no relief' framing over-asserts on a fact-dependent merits issue.
- `G5`: The answer correctly invokes Delaware § 262, but 'these rights generally apply to NYSE-listed corporations' omits the market-out rule and cash-consideration exception; its categorical claim that a proper process means appraisal claims 'provide no relief' also overstates the effect of deal-price evidence. The citation lacks the governing subsections, and the answer substitutes valuation speculation for eligibility guidance, omitting § 262(g), continuous holding, no favorable vote, and the dispositive pre-vote written-demand deadline—the latter triggering critical failure.

---

## COR-05 — Corporate / tax (US - federal)

**Question.** Our private portfolio company is being acquired and several executives have change-of-control payments. What is the 280G exposure and is there anything we can do about it?

**Trap.** Describing the 3x trigger but omitting that the tax falls on the excess over the base amount, or offering the shareholder vote to a public company.

**Answer under test** (`A_standard`):

> Section 280G imposes a 20% excise tax on executives receiving change-of-control payments exceeding 3x their base compensation plus average annual benefits (the "3x trigger"). The company may also lose tax deductions for excess payments. For private company acquisitions, this is frequently overlooked but can be catastrophic. Mitigation strategies include: (1) obtaining written 280G gross-up waivers from executives, reducing their severance accordingly; (2) restructuring payments to remain below the 3x trigger; (3) timing payments post-closing; or (4) obtaining a fairness opinion supporting the severance as reasonable independent of the change. 280G calculations are complex; engage a specialized valuation firm immediately to assess exposure and model mitigation strategies.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 0 | +1 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 0 | +1 |
| D5 Scope discipline | 1 | 0 | +1 |
| Critical failure | False | True | **SPLIT** |

- `G4`: Misstates the mechanics: says the 20% excise tax applies to payments 'exceeding 3x their base compensation' rather than to the excess over the base amount once the 3x threshold is crossed, and misdefines the base amount as 'base compensation plus average annual benefits' instead of the five-year average W-2 compensation; it also mislabels the excise tax as arising under 280G rather than IRC 4999. It omits the single most important private-company remedy — the 280G(b)(5) shareholder cleansing vote (>75% approval with waiver) — and substitutes invented fixes ('280G gross-up waivers,' 'timing payments post-closing,' a 'fairness opinion'), cites no provisions beyond a bare '280G,' and closes with directive 'engage a valuation firm immediately' advice built on the flawed framework.
- `G5`: The answer correctly stays within US federal law, but 'Section 280G imposes a 20% excise tax' misattributes IRC 4999's tax, while 'exceeding 3x their base compensation plus average annual benefits' misstates the threshold and base calculation and omits taxation of the excess over one base amount. It mentions cutbacks but omits the private-company shareholder cleansing procedure and its requirements, and recommends 'timing payments post-closing' and a 'fairness opinion' as mitigation without explaining that neither alone prevents 280G exposure, making the directive advice misleading.

---

## EMP-01 — Employment (US - federal + state)

**Question.** We have a 'Marketing Manager' paid a $52,000 salary who supervises no one and spends most of her time executing campaigns. Is she exempt from overtime?

**Trap.** Asserting a specific current federal salary threshold as settled, or resolving exempt status from the title alone.

**Answer under test** (`A_standard`):

> Under the Fair Labor Standards Act and most state wage-and-hour laws, exempt status depends on the "duties test," not title or salary alone. A Marketing Manager executing campaigns with no supervisory authority almost certainly fails the "executive" exemption test (requiring management of employees or department). She might qualify for a "creative professional" exemption if her role involves substantial independent creative judgment, but this is fact-specific and rarely applies to campaign execution. At $52,000, salary may exceed current federal thresholds (currently $844/week), but thresholds continue rising. She is almost certainly non-exempt and entitled to overtime compensation. Misclassification exposes the company to back-pay liability, penalties, and attorney fees. Reclassify her immediately and audit similar positions.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 1 | +1 |
| D2 Jurisdictional grounding | 1 | 1 | +0 |
| D3 Issue completeness | 2 | 1 | +1 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 2 | 0 | +2 **<-** |
| Critical failure | False | True | **SPLIT** |

- `G4`: Correctly reasons that duties defeat the executive exemption and that title is irrelevant, but asserts '$844/week' as the current federal threshold — a figure that has been enjoined/vacated and is exactly the trap the gold reference flags — and omits the administrative exemption's discretion-and-independent-judgment analysis; it also never mentions state overlays (California/New York higher thresholds) despite the question being framed as federal + state, and cites no authority (no 29 U.S.C. 213(a)(1), no 29 C.F.R. Part 541) while stating the FLSA lookback/liquidated damages only vaguely as 'penalties.'
- `G5`: The assertion 'currently $844/week' with 'thresholds continue rising' incorrectly treats a displaced federal threshold as operative, triggering critical failure; 'most state wage-and-hour laws' omits higher state thresholds and the more-protective-standard rule, and no governing provision is cited. Although the answer correctly discounts title and identifies the executive-exemption problem, it omits salary-basis requirements, the administrative-exemption analysis, liquidated damages, and the two-/three-year lookback, while 'Reclassify her immediately' gives unsupported directive advice without establishing her actual duties or applicable state law.

---

## EMP-02 — Employment (US - California)

**Question.** Can we enforce a one-year, 25-mile non-compete against a California-based employee if our employment agreement is governed by Texas law?

**Trap.** Applying a reasonableness / blue-pencil analysis, or assuming the Texas choice-of-law clause resolves it.

**Answer under test** (`B_terse`):

> No. California Public Code Section 16600 voids all non-competes regardless of choice of law. Texas choice of law doesn't override California public policy. The clause is unenforceable in any forum.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 1 | +1 |
| D2 Jurisdictional grounding | 2 | 1 | +1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 0 | +1 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | False | True | **SPLIT** |

- `G4`: Core conclusion ('No... voids all non-competes regardless of choice of law') is correct and avoids the reasonableness/blue-pencil trap, but 'California Public Code Section 16600' misnames the Business and Professions Code and the flat claim that the clause is 'unenforceable in any forum' overstates the position without reference to Labor Code 925 or Section 16600.5; omits SB 699/AB 1076, the private right of action and attorney's fees, the notice obligation, and the trade-secret/non-solicit carve-outs, and cites no case such as Edwards v. Arthur Andersen, giving a bare conclusion with no fact-dependent qualifications or next steps.
- `G5`: The answer correctly rejects reliance on Texas choice of law, but 'voids all non-competes regardless of choice of law' and 'unenforceable in any forum' materially overstate the rule without identifying relevant factual qualifications; it also omits the Labor Code 925 overlay, the 2024 legislation, remedies and notice obligations, and trade-secret/customer-nonsolicit distinctions. 'California Public Code Section 16600' cites a nonexistent code rather than Business and Professions Code section 16600, triggering the authority critical failure.

---

## EMP-06 — Employment (US - California + federal)

**Question.** We engage software developers in California as 1099 contractors. They use our tools, work our hours, and only work for us. Is that defensible?

**Trap.** Applying only the IRS control test, or blending the ABC and economic-realities tests as if they were one standard.

**Answer under test** (`B_terse`):

> This is likely misclassification. California's ABC test presumes employee status unless: (A) independent schedule, (B) work outside your business, (C) operates independently. These contractors fail all three. Reclassify or face wage-and-hour penalties.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 1 | +1 |
| D2 Jurisdictional grounding | 2 | 1 | +1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 2 | 0 | +2 **<-** |
| Critical failure | False | False | - |

- `G4`: Correctly identifies the ABC test and reaches the right bottom line, but paraphrases prong A as 'independent schedule' rather than freedom from control and asserts the contractors 'fail all three' without noting prong B is the decisive failure or that prong C is fact-dependent; no mention of Borello's continuing role, and the federal side of the question (DOL economic-realities / IRS common-law tests, and the possibility of divergent classification) is entirely omitted despite the question naming federal law. Cites no authority at all — no Lab. Code 2775, Dynamex, or 2802 — and gives no exposure detail (overtime, expense reimbursement, PAGA) or concrete next step beyond 'reclassify.'
- `G5`: The answer reduces ABC prong A to an 'independent schedule' and asserts that the developers 'fail all three' without establishing the company's usual business; it omits Borello exemptions, separate federal DOL and IRS analyses, and the specified exposures beyond generic wage-and-hour penalties. It cites no governing authority, and 'Reclassify or face wage-and-hour penalties' gives categorical directive advice without assessing facts or exemptions that could change the result.

---

## LIT-03 — Litigation procedure (US - federal / constitutional)

**Question.** Our client is sued in Montana over a product it sold nationwide but not specifically into Montana; the particular unit was resold there by a third party. Can the court exercise specific personal jurisdiction?

**Trap.** Applying a but-for causation requirement and concluding there is no jurisdiction because the defendant did not sell that unit into the forum.

**Answer under test** (`A_standard`):

> This implicates specific personal jurisdiction under International Shoe Co. v. Washington. A court may exercise specific jurisdiction if: (1) the defendant has a substantial connection to the forum, (2) the claim arises from that connection, and (3) exercise is reasonable. Your client's position is weak: it sold nationwide but not to Montana; the unit reached Montana through third-party resale. Most courts hold this insufficient for specific jurisdiction because your client did not "purposefully avail" itself of Montana by directing sales there. The resale is a superseding act. Absent evidence that your client knew the product would reach Montana or directed it there, specific jurisdiction likely fails. General jurisdiction also fails absent physical presence in Montana. This is a solid motion-to-dismiss argument.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 0 | 0 | +0 |
| D2 Jurisdictional grounding | 1 | 3 | -2 **<-** |
| D3 Issue completeness | 0 | 1 | -1 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 0 | 0 | +0 |
| Critical failure | True | True | - |

- `G4`: The answer walks directly into the gold trap by requiring a causal link ('the claim arises from that connection,' 'The resale is a superseding act,' 'Absent evidence that your client knew the product would reach Montana... specific jurisdiction likely fails'), which is the opposite of Ford Motor Co. v. Montana (2021) — a case arising from these very facts and never cited; it also misstates general jurisdiction as turning on 'physical presence' rather than Daimler's incorporation/PPB test, omits Bristol-Myers Squibb and the claim-by-claim/fair-play analysis, and concludes with directive advice ('This is a solid motion-to-dismiss argument') that would mislead a reader.
- `G5`: The answer applies the correct federal constitutional framework but treats resale as a 'superseding act' and requires that the claim 'arises from' forum contacts, omitting Ford's relates-to rule; 'General jurisdiction also fails absent physical presence' incorrectly substitutes physical presence for Daimler's at-home test. Although it mentions purposeful availment and reasonableness, it omits the governing Ford, Bristol-Myers Squibb, and Daimler authorities and claim-by-claim/defendant-by-defendant analysis, while calling dismissal 'solid' without establishing the defendant's Montana market activities or the plaintiff's forum connection.

---

## IPR-01 — Intellectual property (US - federal)

**Question.** We hired a freelance designer to create our logo and the invoice says 'work made for hire.' Do we own the copyright?

**Trap.** Answering yes because the document says 'work made for hire.'

**Answer under test** (`A_standard`):

> Not necessarily. Although the invoice references "work made for hire," this language alone is insufficient under U.S. copyright law. A "work made for hire" requires either: (1) a written agreement signed by the creator before or at the time of creation, OR (2) work falling within specific categories (e.g., employee works in scope of employment). An invoice signed after creation is typically ineffective to establish work-made-for-hire status. The correct approach is a separate written copyright assignment. To secure ownership, obtain a written work-made-for-hire agreement or copyright assignment before the designer begins work. If the current document is insufficient, consider a retroactive written assignment. Without proper documentation, you may hold only a license, not ownership of the copyright.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 0 | +1 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 2 | 1 | +1 |
| Critical failure | False | True | **SPLIT** |

- `G4`: The answer misstates the governing rule by framing the test as a disjunctive 'either (1) signed writing OR (2) enumerated categories,' when 17 U.S.C. 101 requires for an independent contractor BOTH a signed writing AND one of the nine enumerated categories — and it never mentions that a logo almost certainly fits none of them, which is the dispositive point; it also cites no authority (no 101, 201(b), 204(a), or CCNV v. Reid) and omits the California Labor Code 3351.5 overlay and the separate trademark analysis, though it correctly avoids the 'yes' trap and gives an actionable next step (written assignment).
- `G5`: The statement that work-made-for-hire status requires a signed agreement 'OR' qualifying work confidently inverts the contractor rule requiring both, triggering critical failure; the answer correctly uses federal copyright law but cites none of the expected governing provisions. It recommends an assignment and questions the invoice's sufficiency, but omits the logo's usual category ineligibility, contractor initial ownership, California consequences, and separate trademark rights, while misleadingly offering a work-made-for-hire agreement as an alternative means 'to secure ownership.'

---

## IPR-02 — Intellectual property (US - federal)

**Question.** We filed an intent-to-use trademark application eight months ago and got a notice of allowance. We have not launched yet. What happens now?

**Trap.** Stating an indefinite extension right or omitting the 36-month outer limit.

**Answer under test** (`B_terse`):

> You have six months from notice of allowance to file a statement of use showing commercial use. If you haven't launched, file an extension request now. One extension is grantable as of right; further extensions require showing good cause.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 2 | 3 | -1 |
| D2 Jurisdictional grounding | 2 | 3 | -1 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 1 | +0 |
| D5 Scope discipline | 1 | 2 | -1 |
| Critical failure | True | False | **SPLIT** |

- `G4`: Core six-month SOU deadline and first-extension-as-of-right are correct, but the answer omits the 36-month outer limit and says only that 'further extensions require showing good cause,' leaving the impression of open-ended extensions — the precise trap named in the gold reference, and a missed dispositive bar; it also omits abandonment/petition-to-revive, the bona fide intent documentation requirement, and priority relation-back, and cites no authority (15 U.S.C. 1051(d), 37 C.F.R. 2.89) despite giving a clean directive ('file an extension request now') without naming the facts or limits that control.
- `G5`: The six-month deadline measured from the notice of allowance and the distinction between the first extension and later good-cause extensions correctly apply federal trademark law, but no governing authority is cited. The answer omits the 36-month cap, extension fees and continued-intent requirements, abandonment and revival, registration and priority consequences, and documentary intent at filing; 'file an extension request now' is actionable but does not establish whether the notice-based deadline remains open.

---

## ETH-02 — Legal ethics / confidentiality (US - state bar rules)

**Question.** May a lawyer put confidential client documents into a third-party generative AI tool?

**Trap.** Answering with a flat prohibition, or a flat permission with no consent or verification analysis.

**Answer under test** (`B_terse`):

> Prohibited without informed consent. Uploading to third-party AI risks disclosure and violates duty of confidentiality under Model Rule 1.6. Client must consent recognizing risks. Use lawyer-only AI services or in-house systems.

| Dimension | `G4` | `G5` | Gap |
|---|---|---|---|
| D1 Legal accuracy | 1 | 1 | +0 |
| D2 Jurisdictional grounding | 1 | 1 | +0 |
| D3 Issue completeness | 1 | 1 | +0 |
| D4 Authority hygiene | 1 | 2 | -1 |
| D5 Scope discipline | 1 | 1 | +0 |
| Critical failure | True | False | **SPLIT** |

- `G4`: "Prohibited without informed consent" states a categorical rule that ABA Formal Op. 512 does not adopt — consent turns on the tool's terms (training use, provider access, self-learning), so presenting it as settled and universal is a confidently inverted/overstated rule and squarely the gold trap; it cites only Rule 1.6 generically with no Op. 512, no Rule 1.1 cmt. 8 competence duty, no 5.1/5.3 supervision, no 1.5 billing, no 3.3 candour or output-verification/fabricated-citation sanctions, and no acknowledgment that state bar opinions (CA, FL, NY) diverge.
- `G5`: “Prohibited without informed consent” materially overstates a tool-dependent requirement, and “Use lawyer-only AI services or in-house systems” offers a categorical recommendation without assessing training, personnel access, or safeguards; the answer also omits nonuniform state-bar requirements. Model Rule 1.6 is relevant but cited imprecisely, while the answer misses Opinion 512, technology competence, supervision, billing, candour, and output verification.

