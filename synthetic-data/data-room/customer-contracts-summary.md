# Horizon Analytics — Customer Contracts Summary (Top 10)

*Prepared by Horizon Analytics legal team. As of March 2026.*

---

## Top 10 Customers by ACV

| # | Customer | Sector | ACV | Contract end | Notice period | Change-of-control clause | Auto-renew |
|---|---|---|---|---|---|---|---|
| 1 | Caledonian Mutual Insurance | Insurance | $620K | Dec 2026 | 90 days | **Yes — consent required** | No |
| 2 | Albion Wealth Partners | Wealth Mgmt | $480K | Jun 2026 | 60 days | **Yes — consent required** | Yes |
| 3 | Stratford Bank | Banking | $410K | Mar 2027 | 90 days | None | Yes |
| 4 | Meridian Life Assurance | Insurance | $390K | Sep 2026 | 90 days | **Yes — consent required** | No |
| 5 | Northgate Pension Fund | Asset Mgmt | $310K | Dec 2026 | 60 days | None | Yes |
| 6 | Blackrock & Reid Advisors | Wealth Mgmt | $275K | Jun 2027 | 30 days | **Yes — right to terminate** | Yes |
| 7 | Forth River Credit Union | Banking | $190K | Sep 2026 | 30 days | None | No |
| 8 | Atlas Capital Management | Asset Mgmt | $175K | Dec 2026 | 60 days | None | Yes |
| 9 | Dorset Building Society | Banking | $165K | Mar 2027 | 60 days | None | Yes |
| 10 | Clyde Underwriting Group | Insurance | $155K | Jun 2026 | 90 days | **Yes — consent required** | No |

**Total top 10 ACV: $3.17M (39.6% of $8.0M ARR)**

---

## Change-of-Control Summary

Five of the top 10 customers (representing $1.93M ACV, ~24% of total ARR) have change-of-control clauses.

| Type | Customers | ACV at risk |
|---|---|---|
| Consent required | Caledonian, Albion, Meridian, Clyde | $1.67M |
| Right to terminate | Blackrock & Reid | $275K |

**Key risk:** If these customers do not consent to the acquisition or exercise termination rights, the deal at $48M EV (6× ARR) may not hold if ARR declines materially post-close.

---

## IP & Data Terms

- All 62 customer contracts include a **data processing agreement (DPA)**.
- 11 DPAs (covering EU-based customers) have not been updated since GDPR amendments in 2023. The specific gap is around the new SCCs (Standard Contractual Clauses) required post-Schrems II.
- Customer data is processed on AWS (eu-west-1 and us-east-1). EU customer data is mapped to eu-west-1 only per current DPAs — but there is no technical enforcement (no egress restriction in place).

---

## Liability and SLA Terms

- Standard customer SLA: 99.9% monthly uptime
- Liability cap: 3× ACV for most contracts; 6× ACV for Caledonian and Stratford Bank (negotiated exceptions)
- No customer has invoked the SLA credit mechanism in 2024 or 2025. Uptime logs show 99.97% average.

---

## Pricing Model

- Annual subscription, billed upfront
- Pricing based on number of active users + data volume tier
- No usage-based metering for HorizonAI module — flat pricing per contract. Management acknowledges this creates margin risk as GPU costs scale.
