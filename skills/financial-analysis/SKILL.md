---
name: financial-analysis
description: M&A financial diligence framework for BTS-Synthetic. Use whenever reviewing a target company's financials for an acquisition — covers quality of revenue, unit economics, burn analysis, valuation sense-check, and red-flag patterns. Trigger on any request to review, assess, or flag a target's financial statements, ARR metrics, or deal economics.
---

# Financial Diligence Framework

Use this framework to analyse a target company's financials during M&A diligence.

## 1. Quality of Revenue

Assess whether reported ARR/revenue is real and durable.

**Checks:**
- Is revenue recurring (subscription) or one-time (services)? What's the split?
- Are contracts annual with upfront billing (high quality) or monthly (churn risk)?
- Is deferred revenue growing proportionally to ARR? If not, investigate.
- What is the revenue recognition policy? Any aggressive capitalisation?

**Red flags:**
- Revenue from a small number of customers (>20% from any one = concentration risk)
- Discounts or one-time terms buried in contracts to hit ARR targets
- Professional services >15% of revenue in a "SaaS" company

## 2. Unit Economics

**Net Revenue Retention (NRR):** Best predictor of sustainable growth.
- >120%: world-class, land-and-expand working
- 100–120%: healthy
- <100%: churning faster than expanding — investigate immediately

**Gross Margin:**
- SaaS: expect 70–80%+ at scale
- If <65%, check for high infrastructure or professional services costs depressing margin

**CAC Payback Period:**
- Calculate: (S&M spend in period) / (new ARR × gross margin)
- <18 months: good
- >24 months: inefficient GTM

## 3. Burn & Runway Analysis

- What is the monthly cash burn (net)?
- How many months of runway at current burn?
- Is burn accelerating? Why?
- Is there a credible path to profitability — what ARR is required and is the growth rate consistent with reaching it?

**Red flags:**
- Runway <12 months without a clear bridge
- Burn accelerating faster than growth
- Capitalised R&D growing as % of revenue (obscures true cash burn)

## 4. Balance Sheet Quality

- Is accounts receivable growing faster than revenue? (Collection risk)
- Are there off-balance-sheet liabilities (operating leases, earnouts)?
- What is the preference stack (liquidation preferences)? Who gets paid first?
- Are there any convertible notes that would dilute the acquirer?

## 5. Valuation Sense-Check

**Common SaaS multiples (2025-2026 market):**
- 4–6× ARR: reasonable for 20–35% growth, moderate profitability path
- 6–10× ARR: requires >40% growth AND strong NRR (>115%)
- >10× ARR: requires category-defining position or strategic premium

**Questions to ask:**
- Does the proposed multiple reflect the growth rate AND the quality of that growth?
- What happens to the multiple if top customers churn (change-of-control risk)?
- Is management's ARR/growth projection for the next 12 months realistic given pipeline?

## Output Format

Structure your output as:

```
FINANCIAL DILIGENCE SUMMARY

Quality of Revenue: [High / Medium / Low]
Key findings:
  - [finding 1]
  - [finding 2]

Unit Economics: [Healthy / Concern / Red Flag]
  NRR: [X%]
  Gross margin: [X%]
  CAC payback: [X months or N/A]

Burn & Runway:
  Monthly burn: $[X]K
  Runway: [X] months
  Path to profitability: [clear / unclear / speculative]

Valuation:
  Proposed EV: $[X]M
  Implied multiple: [X]× ARR
  Assessment: [Fair / Rich / Aggressive]

Top 3 financial risks:
  1. [risk] — severity: [High / Med / Low]
  2. [risk] — severity: [High / Med / Low]
  3. [risk] — severity: [High / Med / Low]

Overall recommendation: [Proceed / Proceed with conditions / Do not proceed]
```
