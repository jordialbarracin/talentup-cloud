# TalentUP® — Zero-Lock-In Single-Tenant Open Source Cloud Orchestrator

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-FF4F00.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Live Demo](https://img.shields.io/badge/Live_Demo-talentup--live-0F0F0F.svg)](https://jordialbarracin.github.io/talentup-live/)
[![EU GDPR Sovereign](https://img.shields.io/badge/Jurisdiction-EU_GDPR_(Germany)-10B981.svg)](https://github.com/jordialbarracin/talentup-cloud)

**TalentUP** is an open-source orchestration, migration, and single-tenant provisioning engine that enables European SMEs to replace US-centric, per-seat proprietary SaaS monopolies (*Salesforce, Jira, Slack, Zendesk, DocuSign, SAP/Holded*) with an isolated, GDPR-native stack of **9 audited Free and Open Source Software (FOSS) suites** running inside a dedicated Single-Tenant capsule.

- **Live Interactive Platform (EN / ES):** [https://jordialbarracin.github.io/talentup-live/](https://jordialbarracin.github.io/talentup-live/)
- **Operator & Telemetry Console:** [https://jordialbarracin.github.io/talentup-live/admin.html](https://jordialbarracin.github.io/talentup-live/admin.html)

---

## 1. The Problem We Solve

While world-class open-source alternatives to proprietary SaaS exist today, **90%+ of European SMEs (10–250 employees) cannot adopt them** due to three critical barriers:
1. **DevOps Complexity:** Non-technical SMEs cannot manually self-host, harden, and maintain 9 separate container stacks, PostgreSQL databases, TLS certificates, and backup pipelines.
2. **Data Migration Friction:** Moving existing business records out of HubSpot/Salesforce, Jira, or Slack into open-source databases requires custom schema mapping.
3. **Cloud Lock-In:** Managed SaaS clouds re-introduce per-seat pricing ($10–$30/user/month) and trap customer data behind proprietary APIs.

**TalentUP** eliminates all three barriers with:
- **45-Second Single-Tenant Capsule Provisioning** (dedicated PostgreSQL 16 + rootless Docker Compose + automatic Caddy TLS per organisation in Frankfurt/Nuremberg).
- **Proprietary-to-FOSS Data Migration Connectors** (1-click schema-validated import from HubSpot, Jira, and Slack).
- **1-Click Sovereign Exit (`Zero Lock-In`)**: Every tenant can export their complete, runnable `docker-compose.yml` and database snapshot via `/api/catalog/{app_id}/compose` at any time to run on their own hardware.

---

## 2. The 9 Audited Open Source Suites

| Suite | Upstream License | Replaces | Core Stack |
| :--- | :--- | :--- | :--- |
| **Twenty CRM** | `AGPLv3` | Salesforce / HubSpot | TypeScript, NestJS, React, PostgreSQL 16 |
| **Plane Projects** | `AGPLv3` | Jira / Linear / Monday | Next.js, Python/Django, Redis, PostgreSQL |
| **Mattermost Team** | `MIT` | Slack Pro / MS Teams | Go, React, PostgreSQL |
| **Documenso Sign** | `AGPLv3` | DocuSign / Adobe Sign | Next.js, Prisma, X.509 eIDAS Certificates |
| **Chatwoot Omni** | `MIT` | Zendesk / Intercom | Ruby on Rails, Vue.js, PostgreSQL, Redis |
| **Odoo CE ERP** | `LGPLv3` | SAP Business One / Holded | Python, Owl JS, PostgreSQL 16 |
| **Cal.com** | `AGPLv3` | Calendly Teams | Next.js, Prisma, PostgreSQL |
| **AFFiNE Workspace** | `MIT` | Notion / Miro | Rust, TypeScript, OctoBase |
| **PostHog OSS** | `MIT` | Mixpanel / Amplitude | Python, ClickHouse, React |

---

## 3. System Architecture

```
+-------------------------------------------------------------------------+
|                    TalentUP Single-Tenant Orchestrator                  |
|  FastAPI Provisioner (02_ENGINEERING/backend/main.py) + SQLite Ledger   |
|  Deterministic Constitutional Validator (03_AGENTS/constitution.py)     |
+------------------------------------+------------------------------------+
                                     |
         +---------------------------+---------------------------+
         |                           |                           |
         v                           v                           v
+-----------------+         +-----------------+         +-----------------+
| Capsule: TenantA|         | Capsule: TenantB|         | Sovereign Exit  |
| - Caddy AutoTLS |         | - Caddy AutoTLS |         | Generator       |
| - Twenty / Plane|         | - Odoo / Documen|         | - Portable YAML |
| - Dedicated PG16|         | - Dedicated PG16|         | - Encrypted SQL |
| - 6h Restic Snap|         | - 6h Restic Snap|         | - Zero Lock-In  |
+-----------------+         +-----------------+         +-----------------+
```

### Repository Structure
- [`02_ENGINEERING/backend/main.py`](02_ENGINEERING/backend/main.py) — FastAPI Single-Tenant Provisioning Engine, Sovereign Exit Docker Compose generator (`/api/catalog/{app_id}/compose`), and Deflationary Arbitrage Ledger.
- [`02_ENGINEERING/frontend/index.html`](02_ENGINEERING/frontend/index.html) — Interactive Scrollytelling Flagship Web UI (English default with instant `EN · ES` switcher).
- [`02_ENGINEERING/frontend/admin.html`](02_ENGINEERING/frontend/admin.html) — Operator & Infrastructure Telemetry Console.
- [`03_AGENTS/constitution.py`](03_AGENTS/constitution.py) & [`03_AGENTS/orchestrator.py`](03_AGENTS/orchestrator.py) — Deterministic safety & SLA rules (`0` critical CVEs, `>=99.90%` uptime SLA, `0.00 €` per-seat markup, automated wholesale hardware cost deflation).
- [`05_DEPLOY/Caddyfile`](05_DEPLOY/Caddyfile) & [`docker-compose.prod.yml`](docker-compose.prod.yml) — Production reverse-proxy and container orchestration templates.

---

## 4. Open Source Roadmap (NLnet Restack Milestones)

1. **Milestone 1 — Open Single-Tenant Provisioning & Isolation Engine:** Declarative capsule provisioner (Docker Compose + isolated PostgreSQL 16 + Caddy automatic TLS + WireGuard private mesh) with zero-downtime rolling updates and automatic snapshot rollback.
2. **Milestone 2 — Open SaaS-to-FOSS Data Migration Bridge:** Schema-validated migration connectors importing CSV/JSON/API exports from HubSpot/Salesforce into Twenty CRM, Jira/Trello into Plane, and Slack into Mattermost.
3. **Milestone 3 — Sovereign Exit & Cryptographic Backup Standard:** Self-contained 1-click exit archive (`docker-compose.yml` + `.env` + `pg_dump`) and 6-hour encrypted Restic/Borg backups with user-held keys.
4. **Milestone 4 — Automated Security Hardening & CVE Gate:** Trivy container vulnerability gate, cgroup v2 tenant memory isolation, and full end-to-end test suite.

---

## 5. Quickstart (Local Development)

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Launch the TalentUP Orchestrator & Web UI on port 8088
python -m uvicorn main:app --app-dir 02_ENGINEERING/backend --host 127.0.0.1 --port 8088
```

Then open:
- **Public Web Platform:** `http://127.0.0.1:8088/`
- **Operator Console:** `http://127.0.0.1:8088/admin.html`
- **Export Sovereign Docker Compose Bundle:** `http://127.0.0.1:8088/api/catalog/twenty/compose?subdomain=acme`

---

## 6. License

Released under the **GNU Affero General Public License v3.0 (AGPL-3.0)** — guaranteeing complete freedom to inspect, self-host, modify, and exit without vendor lock-in.

Author: **Jordi Albarracin i Puig** (`jordialbarracinpuig@gmail.com`)
