# NEXUS OPEN — Arquitectura de la Startup

**Nota del co-fundador:** Voy a ser quirúrgico. Nada de "revolucionamos el mercado". Vamos a construir un negocio que factura desde el mes 1 con márgenes reales, costes auditables y una ventaja competitiva estructural: **cero coste laboral humano en operación**.

---

## 1. TESIS Y MODELO DE NEGOCIO REAL

### 1.1 La tesis en una frase
> Los gigantes SaaS cobran 20-40x el coste real de cómputo porque su P&L está dominado por ventas, marketing y RRHH. Nosotros eliminamos esas tres líneas y alojamos la misma funcionalidad (o superior) sobre Open Source líder, con IA operando la infraestructura.

### 1.2 Sustitución real (no marketing)

| Gigante | Precio real PyME (10 users) | Alternativa OSS | Coste infra real/mes | Precio NEXUS |
|---|---|---|---|---|
| Salesforce | ~€300/mes | **Twenty CRM** | €4.5 (Hetzner CX22) | **€9/mes** |
| Factorial | ~€120/mes | **Odoo CE / ERPNext** | €7.5 (CX32) | **€14/mes** |
| Zendesk | ~€250/mes | **Chatwoot** | €4.5 | **€9/mes** |
| Slack Pro | ~€80/mes | **Mattermost** | €4.5 | **€9/mes** |
| DocuSign | ~€150/mes | **Documenso** | €4.5 | **€9/mes** |
| Jira | ~€80/mes | **Plane** | €4.5 | **€9/mes** |
| **Total** | **~€980/mes** | — | **~€30/mes** | **~€59/mes** |

**Ahorro cliente: ~94%. Margen NEXUS: ~50% bruto sobre infra.**

### 1.3 Modelo de precio (fórmula pública)

```
Precio = Coste_Infra_Real + Coste_Backup + Coste_Observabilidad + Margen_Fijo(35%)
```

- **Coste_Infra_Real**: factura Hetzner/OVH prorrateada por instancia (visible al cliente en su panel).
- **Margen_Fijo**: 35% plano. No hay tiers, no hay "enterprise pricing", no hay upsell oscuro.
- **Sin coste laboral**: la operación la ejecuta el comité IA. El único humano es el fundador (tú) y, cuando escale, 1 SRE de guardia.

### 1.4 Por qué nadie puede competir en precio
1. **Estructura de costes**: un competidor tradicional necesita 1 DevOps por cada ~50 clientes. Nosotros: 1 DevOps por cada ~5.000.
2. **Sin CAC de ventas**: el comparador de ahorro es el vendedor. SEO + boca a boca.
3. **Sin deuda de features**: no construimos software, empaquetamos el mejor OSS existente.
4. **Economía de escala en infra**: al agregar cientos de instancias negociamos con Hetzner/OVH a precio mayorista.

---

## 2. CEO Y COMITÉ DE DIRECCIÓN (IA)

Arquitectura de agentes sobre **LangGraph + Claude/GPT-4o + herramientas MCP**. Cada agente tiene su propio scope, memoria persistente (Postgres + pgvector) y permisos acotados.

### 2.1 CEO IA — "Atlas"
**Rol:** Estrategia, gobernanza, relación con proveedores de infra, decisiones de catálogo.

**Responsabilidades reales:**
- Negociación de contratos con Hetzner/OVH/Cloudflare (vía API + email automatizado).
- Decisión de qué OSS entra/sale del catálogo (basado en input del CPO).
- Aprobación de cambios de precio (con veto humano del fundador).
- Reporting semanal al fundador: MRR, churn, coste por instancia, alertas.

**Herramientas:** `hetzner_api`, `stripe_api`, `email_smtp`, `postgres_read`, `grafana_api`.

**Guardarraíles:** no puede mover dinero >€500 sin aprobación humana. No puede firmar contratos >12 meses.

### 2.2 CTO IA — "Vulcan"
**Rol:** Despliegue, mantenimiento, parches, backups, SRE autónomo.

**Stack de operación:**
- **Docker + Docker Compose** para instancias single-tenant (aislamiento real).
- **K3s** (Kubernetes ligero) para clientes con múltiples apps.
- **Terraform + Ansible** para provisioning en Hetzner/OVH.
- **Traefik** como reverse proxy con TLS automático (Let's Encrypt).
- **Velero + restic** para backups cifrados a Backblaze B2 (€6/TB/mes).

**Ciclo autónomo:**
```
1. Cliente pulsa "Desplegar Twenty CRM" en la web
2. Vulcan: crea VM en Hetzner (API) → instala Docker → despliega stack → configura DNS → emite TLS → healthcheck
3. Tiempo objetivo: <90 segundos
4. Registra coste real en el ledger del CFO
```

**Mantenimiento continuo:**
- Cron cada 6h: `watchtower` chequea nuevas imágenes, aplica parches de seguridad.
- Backup diario 03:00 UTC, retención 30 días.
- Auto-healing: si healthcheck falla 3 veces → reinicia contenedor → si falla 5 veces → escala a humano.

### 2.3 CFO IA — "Ledger"
**Rol:** Facturación al céntimo, optimización de costes, unit economics.

**Funciones:**
- **Ledger de costes por instancia**: cada recurso (VM, GB almacenados, GB transferidos, backups) se registra en Postgres con timestamp.
- **Facturación mensual**: agrega costes reales + margen 35% → emite factura vía Stripe.
- **Optimización continua**: detecta instancias infrautilizadas (<20% CPU/RAM durante 30 días) → propone downgrade → ahorra coste al cliente y mantiene margen.
- **Detección de abuso**: si una instancia consume >3x la media del plan, alerta.

**Transparencia radical:** el cliente ve en su panel el desglose exacto:
```
VM CX22 (Hetzner)         €4.50
Backup B2 (12 GB)         €0.07
Transferencia (8 GB)      €0.00 (incluido)
─────────────────────────────────
Coste real                €4.57
Margen NEXUS (35%)        €1.60
─────────────────────────────────
TOTAL                     €6.17/mes
```

### 2.4 CPO IA — "Curator"
**Rol:** Curaduría y benchmarking continuo del catálogo OSS.

**Funciones:**
- **Scraping diario** de GitHub (stars, commits, issues abiertas, tiempo de resolución, releases).
- **Scoring de proyectos**: `score = f(actividad, comunidad, seguridad, licencia, madurez)`.
- **Benchmarking funcional**: compara features vs. competidor propietario (Salesforce, Jira, etc.).
- **Propuesta al CEO**: "Documenso ha superado a DocuSign en 3 features clave. Recomiendo destacarlo en homepage."
- **Alerta de riesgo**: si un proyecto lleva >90 días sin commits → marca como "en riesgo" → busca alternativa.

**Fuentes:** GitHub API, CVE database, OpenSSF Scorecard, Reddit/HN sentiment.

---

## 3. ESTRUCTURA REAL DEL PRODUCTO Y DE LA WEB

### 3.1 Catálogo clasificado por departamento

```
/ventas-crm        → Twenty, EspoCRM, SuiteCRM
/erp-operaciones   → Odoo CE, ERPNext, Dolibarr
/soporte           → Chatwoot, Zammad, FreeScout
/comunicacion      → Mattermost, Rocket.Chat, Element
/documentos        → Documenso, Paperless-ngx, Nextcloud
/proyectos         → Plane, Vikunja, Focalboard
/analitica         → Metabase, Superset, PostHog
/marketing         → Mautic, Listmonk, Plausible
/rrhh              → OrangeHRM, Odoo HR
/facturacion       → Invoice Ninja, Crater
```

Cada ficha de producto incluye:
- Descripción funcional real (no marketing).
- Comparativa 1:1 con el gigante propietario.
- Coste real de infra + precio NEXUS.
- Botón "Desplegar ahora" (sin registro previo, pago con Stripe).

### 3.2 Comparador de ahorro real

Input del usuario: `nº empleados` + `herramientas que usa actualmente`.
Output: tabla con precio actual estimado (basado en pricing público real, scrapeado por Curator) vs. NEXUS.

**Ejemplo real (10 empleados, stack Salesforce+Slack+Jira):**
```
Actual:  €460/mes
NEXUS:   €27/mes
Ahorro:  €5.196/año (94%)
```

Sin datos inventados: los precios de los gigantes se scrapean semanalmente de sus páginas públicas.

### 3.3 Consola de despliegue

Flujo del cliente:
1. Elige app del catálogo.
2. Selecciona plan (S/M/L → mapea a CX22/CX32/CCX13).
3. Paga con Stripe (suscripción mensual).
4. **Vulcan despliega en <90s**.
5. Cliente recibe email con URL, credenciales admin, y enlace al panel.

**Panel del cliente:**
- Estado de instancias (uptime, CPU, RAM, disco).
- Backups (descargables, restaurables con 1 clic).
- Desglose de costes al céntimo.
- Botón "Actualizar" (aplica última versión OSS).
- Botón "Migrar a otro servidor" (si quiere más potencia).

### 3.4 Panel del Comité Ejecutivo IA (transparencia radical)

Página pública `/comite` donde cualquiera ve:
- **Atlas (CEO)**: últimas decisiones estratégicas, contratos firmados, MRR.
- **Vulcan (CTO)**: nº instancias activas, uptime global, parches aplicados últimas 24h.
- **Ledger (CFO)**: coste medio por instancia, margen medio, facturación del mes.
- **Curator (CPO)**: cambios en el catálogo, proyectos en riesgo, nuevos candidatos.

Esto es **marketing brutal**: nadie más lo hace. Genera confianza y prensa.

---

## 4. ESTRUCTURA DE CÓDIGO DEL PROYECTO

### 4.1 Repositorio (monorepo con Turborepo)

```
nexus-open/
├── apps/
│   ├── web/                    # Next.js 14 (App Router) — web pública + panel cliente
│   ├── api/                    # Fastify + tRPC — API core
│   ├── orchestrator/           # Node.js — Vulcan (despliegues)
│   └── agents/                 # Python — comité IA (LangGraph)
├── packages/
│   ├── db/                     # Prisma + Postgres schema
│   ├── ui/                     # shadcn/ui compartido
│   ├── catalog/                # Definiciones YAML de cada OSS
│   ├── billing/                # Stripe + ledger de costes
│   └── infra/                  # Terraform + Ansible
├── infra/
│   ├── terraform/              # Hetzner, OVH, Cloudflare
│   ├── ansible/                # Playbooks base
│   └── k3s/                    # Manifiestos K8s
└── docs/
```

### 4.2 Backend (`apps/api`)

**Stack:** Fastify + tRPC + Prisma + Postgres + Redis (colas BullMQ).

**Módulos:**
- `auth/` — Clerk o Lucia (auth propia).
- `catalog/` — CRUD de apps OSS.
- `instances/` — ciclo de vida de instancias.
- `billing/` — Stripe webhooks + ledger.
- `agents/` — endpoints que invocan al comité IA.

### 4.3 Orquestador (`apps/orchestrator`) — Vulcan

**Stack:** Node.js + BullMQ + Hetzner SDK + SSH2.

**Jobs:**
```typescript
// pseudocódigo real
async function deployInstance(appId, plan, customerId) {
  const vm = await hetzner.createServer({ type: plan.vmType, location: 'fsn1' });
  await ssh.waitFor(vm.ip);
  await ssh.exec(vm.ip, installDockerScript);
  await ssh.exec(vm.ip, `docker compose -f ${appId}/compose.yml up -d`);
  await traefik.register(vm.ip, `${customerId}.nexusopen.io`);
  await cloudflare.createDNS(`${customerId}.nexusopen.io`, vm.ip);
  await ledger.recordCost(customerId, vm.monthlyCost);
  await notify.customer(customerId, { url, credentials });
}
```

### 4.4 Agentes IA (`apps/agents