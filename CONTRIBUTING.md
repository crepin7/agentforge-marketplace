# Contributing to AgentForge

Merci ! 🎉

## Soumettre un nouvel agent

1. Créez un dossier `agents/<votre-agent>/`
2. Ajoutez `agent.yaml` (name, description, version, pricing)
3. Implémentez `main.py` qui lit stdin JSON et écrit stdout JSON
4. Ajoutez une entrée dans `registry/agents.json`
5. Tests dans `agents/<votre-agent>/tests/`
6. Ouvrez une PR

## Code style

- Backend : `ruff`
- Frontend : `prettier` + `eslint`
- Commits : Conventional Commits
