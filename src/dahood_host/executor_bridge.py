"""Bridge to the Roblox executor (e.g. Synapse-style HTTP endpoint)."""
from __future__ import annotations

import json
from typing import Any

import requests


class ExecutorBridge:
    def __init__(self, endpoint: str = "http://127.0.0.1:55420", timeout: float = 2.0) -> None:
        self.endpoint = endpoint.rstrip("/")
        self.timeout = timeout

    def _post(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.endpoint}{path}"
        resp = requests.post(url, json=payload, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def execute(self, luau_source: str) -> dict[str, Any]:
        return self._post("/execute", {"source": luau_source})

    def health(self) -> bool:
        try:
            r = requests.get(f"{self.endpoint}/health", timeout=self.timeout)
            return r.status_code == 200
        except requests.RequestException:
            return False

    def dump_strings(self) -> list[str]:
        data = self._post("/dump", {"kind": "strings"})
        return json.loads(data.get("result", "[]"))