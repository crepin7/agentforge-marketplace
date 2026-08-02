"""Registry d'agents — auto-decouverte."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any


class AgentRegistry:
    _agents: dict[str, dict[str, Any]] = {}

    @classmethod
    def discover(cls, agents_dir: str, registry_file: str) -> int:
        cls._agents = {}
        reg_path = Path(registry_file)
        if reg_path.exists():
            data = json.loads(reg_path.read_text())
            for agent in data.get("agents", []):
                slug = agent["slug"]
                agent_dir = Path(agents_dir) / slug
                agent["path"] = str(agent_dir)
                agent["available"] = agent_dir.exists() and (agent_dir / "main.py").exists()
                cls._agents[slug] = agent
        return len(cls._agents)

    @classmethod
    def all(cls) -> list[dict[str, Any]]:
        return list(cls._agents.values())

    @classmethod
    def get(cls, slug: str) -> dict[str, Any] | None:
        return cls._agents.get(slug)

    @classmethod
    def available_slugs(cls) -> list[str]:
        return [s for s, a in cls._agents.items() if a.get("available")]
