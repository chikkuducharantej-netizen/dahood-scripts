"""Shared contracts every Da Hood plugin must implement."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(frozen=True)
class PluginMeta:
    name: str
    version: str
    description: str = ""
    author: str = "unknown"
    tags: tuple[str, ...] = ()


class PluginBase(Protocol):
    meta: PluginMeta

    def on_enable(self) -> None: ...

    def on_disable(self) -> None: ...

    def on_tick(self, ctx: "HostContext") -> None: ...


@dataclass
class HostContext:
    """Runtime context passed to plugins each tick."""
    process_handle: Any = None
    place_id: int | None = None
    player_name: str | None = None
    extras: dict[str, Any] = field(default_factory=dict)

    def is_attached(self) -> bool:
        return self.process_handle is not None