# 🔥 AgentForge — AI Agent Marketplace

> **La forge à agents IA spécialisés.** Découvrez, déployez et monétisez des agents IA prêts à l'emploi (trading, code, marketing, data, support…). Un seul abonnement, mille compétences.

---

## 💎 Pourquoi AgentForge ?

- **Marché visé** : AI agents = segment qui explose (50 Mrd$ en 2026, projection 200+ Mrd$ en 2030).
- **Problème** : Les modèles d'IA bruts ne sont pas directement utilisables par des non-tech.
- **Solution** : Une marketplace clé-en-main où chaque agent a un **rôle clair, un pricing transparent, une API unifiée** et un **revenu partagé** pour le créateur.

## 🧠 Agents inclus (MVP)

| Agent | Rôle | Pricing |
|------|------|---------|
| `trader-sage` | Signaux de trading, analyse technique multi-actifs | 49$/mois |
| `code-wizard` | Code review, refactor, génération de tests | 29$/mois |
| `growth-hacker` | Stratégies d'acquisition, A/B tests, copywriting | 39$/mois |
| `data-analyst` | SQL auto, dashboards, insights business | 39$/mois |
| `support-hero` | Support client multilingue 24/7 | 19$/mois |
| `legal-eagle` | Révision de contrats, conformité RGPD | 59$/mois |

## 🏗️ Architecture

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  Next.js 14  │──▶│  FastAPI GW  │──▶│   Agents     │
│  (Web/App)   │   │  (Auth/Bill) │   │ (Pluggable)  │
└──────────────┘   └──────────────┘   └──────────────┘
        │                  │                  │
        ▼                  ▼                  ▼
   Stripe Checkout    Postgres+Redis    OpenAI/Anthropic/
   + Webhooks         (state, billing)  Local LLMs
```

## 🚀 Quick start

```bash
git clone https://github.com/crepin7/agentforge-marketplace.git
cd agentforge-marketplace
docker compose up -d
# Frontend: http://localhost:3000
# API:      http://localhost:8000/docs
```

## 💸 Business model

1. **Abonnement Marketplace** : 99$/mois = accès illimité à tous les agents
2. **Pay-per-call** : 0.02-0.10$ par appel d'agent pour usage ponctuel
3. **Revenue share créateurs** : 70% pour l'auteur, 30% plateforme
4. **Token utilitaire $FORGE** (Q4 2026) : staking, gouvernance, réduction fees
5. **Enterprise** : on-premise, agents custom, SLA

## 📊 Projections (conservateur)

- Year 1 : 1 000 users × 49$/mois ARPU = ~590k$ ARR
- Year 2 : 10 000 users + 50 agents tiers = 6M$ ARR
- Year 3 : token launch + enterprise = 25-50M$ ARR

## 🤝 Contribuer

PRs bienvenues ! Voir `CONTRIBUTING.md`.

## 📜 License

MIT — voir `LICENSE`.
