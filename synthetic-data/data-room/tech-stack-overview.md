# Horizon Analytics — Technology Stack Overview

*Prepared by Engineering. As of April 2026.*

---

## Architecture Summary

HorizonView and HorizonAI are built as separate services sharing a common data layer. The system is hosted on AWS with a UK-first data residency model for EU customers.

```
[Customers] → [CloudFront CDN]
                  ↓
        [Application Layer]
        Next.js 14 (frontend)
        FastAPI (Python 3.11, backend API)
                  ↓
        [Services Layer]
        ┌────────────────────────────────────────┐
        │ HorizonView Service                    │
        │  - Metabase (embedded BI)              │
        │  - dbt Cloud (transformations)         │
        │  - Apache Airflow (orchestration)      │
        └────────────────────────────────────────┘
        ┌────────────────────────────────────────┐
        │ HorizonAI Service                      │
        │  - LangChain 0.2                       │
        │  - Anthropic Claude (claude-sonnet-4-6)│
        │  - pgvector on RDS Postgres            │
        │  - Custom retrieval pipeline           │
        └────────────────────────────────────────┘
                  ↓
        [Data Layer]
        AWS RDS Postgres (primary DB)
        AWS S3 (data lake)
        Snowflake (customer analytics DW)
```

---

## Infrastructure

| Component | Technology | Notes |
|---|---|---|
| Cloud provider | AWS (eu-west-1, us-east-1) | EU data stays in eu-west-1 |
| Containerisation | Docker + ECS Fargate | No Kubernetes — team decision in 2022 |
| CI/CD | GitHub Actions → ECR → ECS | Manual deploy approval required |
| IaC | Terraform 1.5 | Partially adopted — some infra still console-managed |
| Monitoring | Datadog | APM, logs, dashboards |
| Secrets | AWS Secrets Manager | Migrated from .env files in 2025 |

---

## Key Technology Decisions & Technical Debt

### Positive
- **Modern LLM stack.** HorizonAI is well-architected: retrieval-augmented generation with pgvector, Anthropic Claude API, streaming responses. The ML team understands prompt engineering and evals.
- **Snowflake for analytics.** Clean separation between operational DB and analytics warehouse. dbt models are documented.
- **Python 3.11 throughout.** No Python 2 legacy. Dependencies are pinned in `requirements.txt` with automated Dependabot updates.

### Concerns / Technical Debt

1. **No Kubernetes.** ECS Fargate is adequate for current scale but will require re-platforming for large enterprise clients who require on-premise or VPC deployment options. Estimated effort: 3–4 months of infra work.

2. **Metabase version.** Running Metabase v0.48 (EOL as of Jan 2026). Two known CVEs (CVSS 7.2 and 6.5) in the embedded version. No patch timeline confirmed.

3. **Terraform coverage gaps.** ~30% of AWS infrastructure was created via console and not yet imported into Terraform. This creates drift risk and makes disaster recovery harder to test.

4. **HorizonAI rate-limit handling.** The current LangChain integration does not handle Anthropic API rate limits gracefully — it surfaces 429 errors to end users. A retry/backoff layer is on the roadmap but not implemented.

5. **AGPL-licensed dependencies.** HorizonAI's retrieval pipeline uses `faiss` and `sentence-transformers`, both under AGPL or BSD. There is also a dependency on `openai-whisper` (MIT) which was used in a now-removed feature but is still in `requirements.txt`. More concerning: `llama-index` v0.10 (MIT) is used in one module — but the team is unsure if `llama_index.core` includes any AGPL sub-components. **Licensing audit not completed.**

6. **Single region for EU, no DR test.** Data residency is configured correctly in policy, but disaster recovery to a second EU region has never been tested. The RTO/RPO documented in the BCP is aspirational.

---

## Engineering Team

| Role | Count | Notes |
|---|---|---|
| Engineering VPs / Heads | 1 (CTO Priya Sharma) | **Departure risk — 12mo post-close** |
| Staff / Senior Engineers | 8 | 3 focused on HorizonAI ML stack |
| Mid-level Engineers | 14 | |
| Junior Engineers | 9 | High proportion, code review load on seniors |
| QA / SDET | 4 | Manual QA heavy; only 40% test automation coverage |
| DevOps / SRE | 3 | Thin for scale; 1 is contractor |
| Product Managers | 4 | |
| Designers | 3 | |
| Data Scientists | 3 | Own the HorizonAI model evaluation pipeline |

**Retention packages:** 12 senior engineers and the 3 data scientists have been granted retention options (2-year cliff, 4-year vest) as part of the deal structure. CTO has not accepted a retention offer.

---

## Integration Complexity Estimate

Integrating Horizon's stack into BTS-Synthetic's platform:

| Work stream | Effort estimate | Risk |
|---|---|---|
| Data layer unification (Snowflake → BTS DW) | 4–6 months | Medium |
| Auth / SSO integration | 1–2 months | Low |
| ECS → BTS Kubernetes re-platform | 3–4 months | Medium |
| HorizonAI LLM integration into BTS AI platform | 2–3 months | Low (compatible stack) |
| Customer-facing rebrand of Horizon products | 2 months | Low |
| **Total (sequential)** | **~12–15 months** | |
| **Total (parallel, with resourcing)** | **~6–8 months** | |
