"""Registry holding loaded Da Hood script plugins."""
from __future__ import annotations

from typing import Iterator

from .contracts import PluginBase, PluginMeta


class PluginRegistry:
    def __init__(self) -> None:
        self._entries: dict[str, tuple[PluginBase, PluginMeta]] = {}

    def register(self, name: str, plugin: PluginBase, meta: PluginMeta) -> None:
        self._entries[name] = (plugin, meta)

    def get(self, name: str) -> PluginBase | None:
        entry = self._entries.get(name)
        return entry[0] if entry else None

    def items(self) -> Iterator[tuple[str, PluginMeta]]:
        for name, (_, meta) in self._entries.items():
            yield name, meta

    def __len__(self) -> int:
        return len(self._entries)