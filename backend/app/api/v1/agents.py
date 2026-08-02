"""Endpoints marketplace."""
from fastapi import APIRouter, HTTPException
from app.core.registry import AgentRegistry

router = APIRouter()


@router.get("/")
async def list_agents() -> dict:
    return {"count": len(AgentRegistry.all()), "agents": AgentRegistry.all()}


@router.get("/{slug}")
async def get_agent(slug: str) -> dict:
    agent = AgentRegistry.get(slug)
    if not agent:
        raise HTTPException(status_code=404, detail=f"Agent '{slug}' introuvable")
    return agent
