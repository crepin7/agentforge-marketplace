"""Endpoints d'execution d'agents."""
import time
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.core.registry import AgentRegistry
from app.core.runner import run_agent

router = APIRouter()


class RunRequest(BaseModel):
    inputs: dict = Field(default_factory=dict)


class RunResponse(BaseModel):
    agent: str
    outputs: dict
    latency_ms: int
    cost_cents: int


@router.post("/{slug}", response_model=RunResponse)
async def run(slug: str, req: RunRequest) -> RunResponse:
    agent = AgentRegistry.get(slug)
    if not agent:
        raise HTTPException(status_code=404, detail=f"Agent '{slug}' introuvable")
    if not agent.get("available"):
        raise HTTPException(status_code=503, detail="Agent non deploye")
    t0 = time.perf_counter()
    try:
        outputs = await run_agent(agent, req.inputs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur: {e}") from e
    latency_ms = int((time.perf_counter() - t0) * 1000)
    return RunResponse(agent=slug, outputs=outputs, latency_ms=latency_ms, cost_cents=2)
