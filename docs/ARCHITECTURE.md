# Architecture

## Vue d'ensemble

AgentForge est une marketplace d'agents IA avec une architecture **3-tiers** :

1. **Frontend** (Next.js 14, Tailwind, TanStack Query)
2. **API Gateway** (FastAPI, JWT, Stripe)
3. **Agents** (subprocess Python isolés, I/O JSON via stdin/stdout)

## Pourquoi subprocess ?

- Isolation : un agent buggé ne tue pas l'API
- Sandbox future : passage Firecracker / gVisor / Docker
- Multi-langage : Python, Node, ou WASM

## Flux d'un run

```
Client → POST /api/v1/runs/{slug}
  → vérif JWT + quota + billing
  → spawn subprocess: python agents/{slug}/main.py
  → lit stdin (JSON), écrit stdout (JSON)
  → log Postgres, débite quota, retourne
```

## Stack

| Couche | Tech |
|--------|------|
| Front | Next.js 14, TS, Tailwind, TanStack Query |
| API | FastAPI, SQLAlchemy 2 async, Pydantic v2, Redis |
| Auth | JWT (HS256) |
| Billing | Stripe Checkout + Webhooks |
| DB | Postgres 16, Redis 7 |
| Deploy | Docker Compose → Kubernetes |
