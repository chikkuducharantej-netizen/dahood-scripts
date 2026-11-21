"""Runtime session state for a Da Hood script attachment."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

from .player import Player


@dataclass
class Session:
    place_id: int
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    players: dict[int, Player] = field(default_factory=dict)

    def upsert(self, player: Player) -> None:
        self.players[player.user_id] = player

    def alive_players(self) -> list[Player]:
        return [p for p in self.players.values() if p.is_alive]

    def nearest(self, origin: Player) -> Player | None:
        candidates = [p for p in self.alive_players() if p.user_id != origin.user_id]
        if not candidates:
            return None
        return min(candidates, key=origin.distance_to)