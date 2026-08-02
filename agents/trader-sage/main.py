"""Trader Sage — agent de demo."""
import json
import sys


def main() -> None:
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        payload = {}
    inputs = payload.get("inputs", {})
    asset = inputs.get("asset", "BTC").upper()
    horizon = inputs.get("horizon", "1d")

    result = {
        "signal": "BUY",
        "confidence": 0.72,
        "reasoning": (
            f"Momentum haussier detecte sur {asset} ({horizon}). "
            "RSI en zone neutre, MACD croise a la hausse, volume en augmentation."
        ),
        "metadata": {"model": "demo-v1", "asset": asset, "horizon": horizon},
    }
    sys.stdout.write(json.dumps(result))


if __name__ == "__main__":
    main()
