"""Load and persist user config for the Da Hood script host."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

if sys.version_info >= (3, 11):
    import tomllib as _toml
else:
    import tomli as _toml


DEFAULTS: dict[str, Any] = {
    "executor_endpoint": "http://127.0.0.1:55420",
    "overlay": {"enabled": True, "fps": 144},
    "aim_assist": {"enabled": False, "fov": 120.0, "smooth": 0.35},
    "plugins": {"autoload": ["da_hood_esp", "da_hood_aimbot"]},
}


class ConfigService:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._data: dict[str, Any] = dict(DEFAULTS)

    def load(self) -> dict[str, Any]:
        if self.path.exists():
            with self.path.open("rb") as fh:
                user = _toml.load(fh)
            self._merge(self._data, user)
        return self._data

    def get(self, dotted: str, default: Any = None) -> Any:
        node: Any = self._data
        for part in dotted.split("."):
            if not isinstance(node, dict) or part not in node:
                return default
            node = node[part]
        return node

    @staticmethod
    def _merge(base: dict[str, Any], incoming: dict[str, Any]) -> None:
        for k, v in incoming.items():
            if isinstance(v, dict) and isinstance(base.get(k), dict):
                ConfigService._merge(base[k], v)
            else:
                base[k] = v