"""Dynamic plugin loader for Da Hood script extensions."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from .contracts import PluginMeta
from .registry import PluginRegistry


class PluginLoader:
    def __init__(self, root: Path) -> None:
        self.root = root

    def _iter_plugin_files(self):
        if not self.root.exists():
            return
        for entry in sorted(self.root.glob("*.py")):
            if entry.name.startswith("_"):
                continue
            yield entry

    def load_all(self, registry: PluginRegistry) -> None:
        for path in self._iter_plugin_files():
            try:
                self._load_one(path, registry)
            except Exception as exc:  # noqa: BLE001
                print(f"[loader] failed {path.name}: {exc}", file=sys.stderr)

    def _load_one(self, path: Path, registry: PluginRegistry) -> None:
        mod_name = f"dahood_plugin_{path.stem}"
        spec = importlib.util.spec_from_file_location(mod_name, path)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"cannot build spec for {path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[mod_name] = module
        spec.loader.exec_module(module)

        plugin_cls = getattr(module, "PLUGIN", None)
        if plugin_cls is None:
            raise RuntimeError("missing PLUGIN symbol")

        instance = plugin_cls()
        meta = getattr(instance, "meta", None) or PluginMeta(
            name=path.stem, version="0.0.0", description=""
        )
        registry.register(meta.name, instance, meta)