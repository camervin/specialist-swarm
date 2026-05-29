---
name: tech-stack-assessment
description: M&A technical diligence framework for BTS-Synthetic. Use when evaluating a target company's engineering architecture, technology choices, and integration complexity for an acquisition. Covers scalability, security posture, technical debt, and integration effort. Trigger on any request to assess, evaluate, or flag technical risk in an M&A context.
---

# Technical Diligence Framework — M&A

Use this framework to assess an acquisition target's technology stack and integration complexity.

## 1. Architecture Health

**What to assess:**
- Is the architecture well-structured and documented, or ad-hoc?
- Is there separation of concerns (frontend, backend, data layer)?
- Are there single points of failure in the architecture?
- Is the system cloud-native, or does it rely on legacy on-premise components?

**Scoring:**
- Modern, documented, cloud-native: LOW integration risk
- Partially modernised with known gaps: MEDIUM
- Legacy, monolithic, or poorly documented: HIGH

## 2. Scalability & Performance

**What to assess:**
- What are the current traffic/data volume levels?
- At what scale does the current architecture break? Has this been tested?
- Is autoscaling in place for variable workloads?
- Are there known performance bottlenecks?

**Red flags:**
- No load testing data available
- Architecture can't handle 5× current load without significant re-platforming
- Single-region with no failover

## 3. Security Posture

**What to assess:**
- How are secrets managed (env files, secrets manager, vault)?
- Is infrastructure managed as code (Terraform, Pulumi) or via console?
- Are there known CVEs in the current stack?
- What is the vulnerability management process?
- Has a penetration test been conducted in the past 24 months?

**Red flags:**
- Secrets in source code or unmanaged .env files: HIGH
- Known unpatched CVEs (CVSS >7): HIGH
- No IaC coverage (manual infra = drift and audit risk): MEDIUM
- No recent pen test: MEDIUM

**BTS-Synthetic requirements:**
- All acquired systems must pass BTS-Synthetic's security review within 6 months of close
- SOC 2 Type II readiness required within 12 months

## 4. Test Coverage & Code Quality

**What to assess:**
- What percentage of code is covered by automated tests?
- Is there a CI/CD pipeline with automated testing gates?
- What is the deployment frequency and mean time to recovery (MTTR)?
- Are there documented engineering standards and code review practices?

**Benchmarks:**
- >70% test coverage: LOW risk
- 40–70%: MEDIUM (acceptable with a plan)
- <40%: HIGH — manual QA dependency creates velocity and quality risk post-acquisition

## 5. Key Person Dependency

**What to assess:**
- Is architecture knowledge concentrated in one or two people?
- Is documentation sufficient that the team could onboard new engineers without the original architects?
- What happens if the CTO or lead architect leaves on day 1?

**Red flags:**
- No architecture documentation (or documentation is a person): HIGH
- Critical systems built by contractors who are no longer engaged: HIGH

## 6. Integration Complexity

Estimate the effort required to integrate the target into BTS-Synthetic's platform:

| Work stream | Estimate | Risk level |
|---|---|---|
| Auth / SSO integration | 1–2 months | Low |
| Data layer unification | variable | Medium–High |
| Re-platforming (if needed) | variable | High |
| API / SDK alignment | variable | Medium |
| Customer-facing rebrand | 1–2 months | Low |

**Total integration estimate:** Provide a best-case (parallel) and worst-case (sequential) timeline.

## Output Format

```
TECHNICAL DILIGENCE SUMMARY

Architecture Health: [Good / Acceptable / Concerning]
Scalability: [Ready / Needs work / Risk]
Security posture: [Strong / Adequate / Gaps found]
Test coverage: [X%] — [Low / Medium / High risk]
Key person dependency: [Low / Medium / High]

Key technical issues:
  1. [issue] — severity: [High / Med / Low] — remediation: [X months]
  2. [issue] — severity: [High / Med / Low] — remediation: [X months]
  3. [issue] — severity: [High / Med / Low] — remediation: [X months]

Integration estimate:
  Best case (parallel teams): [X] months
  Worst case (sequential): [X] months
  Most significant blocker: [description]

Overall technical recommendation: [Proceed / Proceed with conditions / Do not proceed]
Conditions: [list any required pre-close technical actions]
```
