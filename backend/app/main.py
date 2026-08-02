"""AgentForge — FastAPI entrypoint."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import agents, auth, billing, runs
from app.core.config import settings
from app.core.registry import AgentRegistry


@asynccontextmanager
async def lifespan(app: FastAPI):
    AgentRegistry.discover("./agents", "./registry/agents.json")
    yield


app = FastAPI(
    title="AgentForge API",
    description="Marketplace d'agents IA specialises",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(agents.router, prefix="/api/v1/agents", tags=["agents"])
app.include_router(runs.router, prefix="/api/v1/runs", tags=["runs"])
app.include_router(billing.router, prefix="/api/v1/billing", tags=["billing"])


@app.get("/health", tags=["meta"])
async def health() -> dict:
    return {"status": "ok", "service": "agentforge", "version": "0.1.0"}


@app.get("/", tags=["meta"])
async def root() -> dict:
    return {"name": "AgentForge", "tagline": "La forge a agents IA specialises", "docs": "/docs"}
