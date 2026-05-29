---
name: people-culture
description: M&A people and culture diligence framework for BTS-Synthetic. Use when assessing a target company's leadership, talent, retention risk, culture fit, and compensation for an acquisition. Covers key person risk, ESOP mechanics, culture signals, and integration readiness. Trigger on any request to assess people risk, retention, culture fit, or leadership in an M&A context.
---

# People & Culture Diligence Framework — M&A

Use this framework to assess talent, leadership, and cultural fit in M&A diligence.

## 1. Leadership Assessment

**What to assess:**
- Which founders/executives are committed to staying post-close?
- Are there clear successors for any departing leaders?
- What is the leadership team's experience with integration and scale?
- Do any executives have conflict-of-interest (e.g., investing in a competitor, advisory roles)?

**Red flags:**
- CTO or CPO indicating departure with no succession plan: HIGH — especially if product architecture is undocumented
- CEO commitment contingent on earnout terms only: MEDIUM — incentive misalignment risk
- Leadership team is all founders (no professional management): MEDIUM for scale risk

**BTS-Synthetic position:** We expect at least 80% of the executive team to remain committed for 24 months post-close. Retention packages should be structured accordingly.

## 2. Key Person Risk

**Identify critical individuals:**
- Who built the core product? Who maintains it?
- Who owns the key customer relationships?
- Who owns the ML/AI model development?

**Assessment levels:**
- BUS (Bus factor 1 — one person's departure kills the function): BLOCKER
- High dependency with a reasonable backup: HIGH
- Distributed knowledge: LOW

**For each high/blocker-risk individual, assess:**
1. Have they accepted a retention offer?
2. If leaving, what is the knowledge transfer plan?
3. Can knowledge be extracted into documentation before close?

## 3. Retention Economics

**ESOP / Equity:**
- What percentage of employees hold meaningful equity (>$50K estimated value at proposed EV)?
- Does the acquisition trigger single-trigger acceleration? (Expensive for acquirer)
- Are there underwater options that reduce retention incentive?

**Retention bonuses:**
- Has the target issued retention packages pre-close?
- Which employees have accepted?
- What is the vesting schedule? (2-year cliff preferred)

**Compensation competitiveness:**
- Is base compensation at or above market benchmarks?
- If below market, will the acquirer need to true-up compensation at close?

## 4. Culture Signals

**Proxy metrics (from available data):**
- **eNPS (employee Net Promoter Score):** >30 is healthy; <20 suggests morale issues
- **Voluntary attrition rate:** <12% is healthy for tech; >18% suggests cultural or compensation problems
- **Glassdoor rating (if public):** <3.5 is a yellow flag

**Cultural compatibility checklist:**
- Is the target remote-first or office-first? (Friction if mismatched with acquirer)
- What is the decision-making style (founder-led vs. process-driven)?
- Are engineering and product teams integrated or siloed?
- What is the attitude toward documentation and process? (Ad-hoc vs. structured)

**BTS-Synthetic culture baseline:**
- Process-oriented, structured
- Documentation-first (Notion-heavy)
- Distributed / remote-friendly
- Outcome-driven performance culture

## 5. Integration Readiness

**People integration checklist:**
- Will the target's teams sit within BTS-Synthetic's existing org structure, or be kept as a standalone unit?
- Are there overlapping roles that will require redundancy decisions?
- What is the communication plan for the target's employees at announcement?
- Who owns the Day 1 integration plan on the people side?

**Headcount overlap risk:**
- G&A overlap (Finance, HR, Legal): typically 50–80% redundancy for integrated acquisitions
- GTM overlap: depends on customer segment alignment
- Engineering: typically retain most, especially in specialist areas

## Output Format

```
PEOPLE & CULTURE DILIGENCE SUMMARY

Leadership commitment: [X of Y executives committed for 24mo]
Key gaps: [list any uncommitted leaders with departure risk]

Key person risk:
  [Name] — [role] — risk: [Bus factor / High / Medium / Low]
  [Name] — [role] — risk: [Bus factor / High / Medium / Low]

Retention economics:
  Retention offers issued: [X employees]
  Accepted: [X]
  ESOP acceleration type: [single / double trigger]
  Compensation vs. market: [above / at / below]

Culture signals:
  eNPS: [X] — [Healthy / Adequate / Concern]
  Voluntary attrition: [X%] — [Healthy / Elevated / Red flag]
  Remote/in-office alignment with BTS-Synthetic: [Aligned / Misaligned]
  Overall culture fit: [Strong / Moderate / Weak]

Integration readiness:
  Estimated redundant headcount (G&A): [X FTE]
  Recommended org structure: [standalone unit / integrated]
  Day 1 comms owner: [name or TBD]

Top 3 people risks:
  1. [risk] — severity: [High / Med / Low]
  2. [risk] — severity: [High / Med / Low]
  3. [risk] — severity: [High / Med / Low]

Overall people recommendation: [Proceed / Proceed with conditions / Do not proceed]
Conditions: [list any required pre-close people actions]
```
