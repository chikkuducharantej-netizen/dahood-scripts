"""Player model extracted from Da Hood memory state."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    user_id: int
    position: tuple[float, float, float]
    health: int = 100
    team: str = "neutral"

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def distance_to(self, other: "Player") -> float:
        ax, ay, az = self.position
        bx, by, bz = other.position
        return ((ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2) ** 0.5