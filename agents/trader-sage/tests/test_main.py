"""Tests de l'agent trader-sage."""
import json
import subprocess
import sys
from pathlib import Path

AGENT_DIR = Path(__file__).parent.parent


def test_trader_sage_runs():
    payload = json.dumps({"inputs": {"asset": "BTC", "horizon": "1d"}})
    result = subprocess.run(
        [sys.executable, "main.py"],
        input=payload.encode(),
        capture_output=True,
        cwd=str(AGENT_DIR),
        timeout=10,
    )
    assert result.returncode == 0, result.stderr.decode()
    out = json.loads(result.stdout.decode())
    assert out["signal"] in {"BUY", "SELL", "HOLD"}
    assert 0 <= out["confidence"] <= 1
    assert out["metadata"]["asset"] == "BTC"
