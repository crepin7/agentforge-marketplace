"""Execute un agent dans un subprocess (sandbox MVP)."""
from __future__ import annotations
import asyncio
import json
import sys
from pathlib import Path


async def run_agent(agent: dict, inputs: dict) -> dict:
    agent_path = Path(agent["path"])
    main_py = agent_path / "main.py"
    if not main_py.exists():
        return {"error": "main.py manquant", "agent": agent["slug"]}

    payload = json.dumps({"inputs": inputs})
    proc = await asyncio.create_subprocess_exec(
        sys.executable, str(main_py),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=str(agent_path),
    )
    try:
        stdout, stderr = await asyncio.wait_for(
            proc.communicate(payload.encode()), timeout=30
        )
    except asyncio.TimeoutError:
        proc.kill()
        return {"error": "timeout (30s)"}

    if proc.returncode != 0:
        return {"error": stderr.decode()[:500]}

    try:
        return json.loads(stdout.decode())
    except json.JSONDecodeError:
        return {"raw": stdout.decode()[:1000]}
