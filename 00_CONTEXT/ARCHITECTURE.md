# ARQUITECTURA TÉCNICA DEL SISTEMA

## 1. Stack Tecnológico Base
* **Runtime de Agentes y Backend Core:** Python 3.11+ con **FastAPI** (asíncrono, alta concurrencia, tipado Pydantic).
* **Motor de Inferencia de IA:**
  * Endpoint: `https://api.tokenfactory.nebius.com/v1/`
  * Modelos primarios:
    * `nvidia/Nemotron-3-Ultra-550b-a55b` (Árbitro, Constitución, Auditoría financiera y técnica)
    * `nvidia/Nemotron-3_5-Lightning` (Clasificación de alta velocidad, embeddings, parsing de tickets)
* **Base de Datos & Auditoría:** PostgreSQL con extensiones de seguridad y registro de eventos inmutable (Audit Trail con hash criptográfico para garantizar transparencia contable ante los clientes).
* **Frontend y Dashboard de Transparencia:** Next.js (React / Tailwind / shadcn/ui minimalista y sobrio, enfocado en alta densidad de datos tipo Bloomberg/Linear).

---

## 2. Diagrama de Módulos del Monorepo

```
00_STARTUP_SAAS/
├── 00_CONTEXT/          <- Documentos de alineamiento y persistencia para IAs
├── 01_PRODUCT/          <- Specs funcionales del Micro-SaaS
├── 02_ENGINEERING/
│   ├── backend/         <- API REST, motor de la Constitución y lógica SaaS
│   └── frontend/        <- Dashboard público y consola de clientes
├── 03_AGENTS/           <- Orquestador y contratos de los 4 agentes (CEO/CPO/CFO/CTO)
├── 04_CONFIG/           <- Variables de entorno (.env) y perfiles de despliegue
└── 05_DOCS/             <- Pitch y guías de usuario
```
