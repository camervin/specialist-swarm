---
name: legal-diligence
description: M&A legal diligence checklist for BTS-Synthetic. Use when reviewing a target company's contracts, IP, and regulatory exposure for an acquisition — covers change-of-control clauses, IP ownership, GDPR/data compliance, open-source licensing, employment obligations, and litigation. Trigger on any request to review, flag, or assess contractual or legal risk in an M&A context.
---

# Legal Diligence Checklist — M&A

Use this checklist when conducting legal diligence on an acquisition target. Flag every issue with severity and recommended action.

## 1. Change-of-Control Clauses

**What to check:**
- Which customer contracts contain change-of-control provisions?
- Do they require consent, or give the customer a right to terminate?
- What is the ACV at risk if consent is withheld or termination exercised?

**BTS-Synthetic position:**
- Any single customer >5% of ARR with a change-of-control right is a material risk.
- Consent-required clauses must be worked through pre-close or price adjusted accordingly.
- Termination rights: model the worst-case revenue impact before signing.

**Severity:**
- >20% of ARR at risk: BLOCKER (renegotiate or price down)
- 10–20% of ARR at risk: HIGH — requires customer outreach plan pre-close
- <10% of ARR at risk: MEDIUM — manageable post-close

## 2. IP Ownership

**What to check:**
- Does the company own all IP in its product, or has any been licensed from a third party?
- Have all employees and contractors signed IP assignment agreements?
- Are there any joint IP claims from a former development partner or university?
- Are there pending patents, and who is named as inventor?

**Red flags:**
- Any IP not fully owned by the company (shared ownership = acquirer's rights are limited)
- Contractor-built code without written IP assignment → acquirer may not own the product
- University involvement in early R&D (common for AI/ML companies) → check license terms

## 3. Open-Source & Software Licensing

**Copyleft licenses (AGPL, GPL):** If the target's product includes AGPL/GPL code and is distributed to customers, the entire product may need to be open-sourced. This is a BLOCKER for most SaaS acquisitions.

**Permissive licenses (MIT, Apache 2.0, BSD):** Generally fine; attribution and patent grant terms still need review.

**What to check:**
- Run an SBOM (Software Bill of Materials) scan on the codebase.
- Identify any AGPL or GPL dependencies in production code.
- Check if any dependencies are dual-licensed (often AGPL for open-source, commercial for SaaS — need to verify the commercial license).

**Severity:**
- AGPL in distributed product with no commercial license: BLOCKER
- Unresolved SBOM (no audit completed): HIGH — must be completed before close

## 4. GDPR & Data Privacy

**What to check:**
- Are all customer DPAs up to date with current SCCs (post-Schrems II standard)?
- Is data residency enforced technically (not just contractually)?
- Has the company conducted a Data Protection Impact Assessment for high-risk processing?
- Is there a documented Data Breach response procedure, and has it been tested?
- Who is the Data Protection Officer (DPO)? Is it an internal role or external?

**BTS-Synthetic position:**
- All DPAs must use current SCCs before close. Outdated DPAs create regulatory exposure for the acquirer from day 1.
- Technical enforcement of data residency (not just policy) is required for regulated-industry customers.

**Severity:**
- Outdated SCCs for EU customers: HIGH — must be remediated before close
- No technical data residency enforcement: MEDIUM — remediation plan required

## 5. Employment & Retention

**What to check:**
- Are key employee contracts in place (offer letters, invention assignment)?
- Are any employees subject to non-competes that would affect post-close work?
- Are there pending employment disputes, unfair dismissal claims, or PIPs?
- What are the terms of the ESOP, and does the acquisition trigger acceleration?

**Vesting acceleration on change-of-control:**
- Single-trigger (acquisition = full vest): expensive for acquirer
- Double-trigger (acquisition + termination = vest): standard, preferred
- Check the ESOP plan rules — this directly affects the retention economics.

## 6. Litigation & Regulatory

**What to check:**
- Any pending or threatened litigation (customer disputes, employment, IP)?
- Any regulatory investigations (FCA, ICO, HMRC)?
- Customer SLA breach claims outstanding?

**Red flags:**
- Active IP infringement claim against the target: BLOCKER until resolved
- Regulatory investigation by data protection authority: HIGH — acquirer may inherit liability

## Output Format

```
LEGAL DILIGENCE SUMMARY

Change-of-Control:
  ACV at risk: $[X]K ([X]% of ARR)
  Severity: [Blocker / High / Medium / Low]
  Action: [renegotiate pre-close / price adjustment / post-close management]

IP Ownership:
  Status: [Clean / Issues found]
  Issues: [list]

Open-Source Licensing:
  AGPL/GPL in product: [Yes / No / Unknown]
  Action required: [SBOM audit / clean / none]

GDPR:
  Outdated DPAs: [X customers]
  Technical residency enforcement: [Yes / Partial / No]
  Action: [remediate before close / post-close plan]

Employment:
  Key person risk: [list]
  Retention options in place: [Yes / Partial / No]

Litigation / Regulatory:
  Open matters: [list or "None"]

Top 3 legal risks:
  1. [risk] — severity: [Blocker / High / Med / Low]
  2. [risk] — severity: [Blocker / High / Med / Low]
  3. [risk] — severity: [Blocker / High / Med / Low]

Overall legal recommendation: [Proceed / Proceed with conditions / Do not proceed]
```
