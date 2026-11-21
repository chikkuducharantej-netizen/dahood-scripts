"""Aim assist helpers used by Da Hood combat plugins."""
from __future__ import annotations

import math

from .esp_overlay import Box


class AimAssist:
    def __init__(self, fov: float = 120.0, smooth: float = 0.35) -> None:
        self.fov = fov
        self.smooth = smooth

    def _center(self, b: Box) -> tuple[float, float]:
        return (b.x + b.w / 2.0, b.y + b.h / 2.0)

    def pick_target(self, boxes: list[Box], cursor: tuple[int, int]) -> Box | None:
        cx, cy = cursor
        best: tuple[float, Box] | None = None
        for b in boxes:
            tx, ty = self._center(b)
            dist = math.hypot(tx - cx, ty - cy)
            if dist <= self.fov and (best is None or dist < best[0]):
                best = (dist, b)
        return best[1] if best else None

    def step_towards(self, cursor: tuple[int, int], target: tuple[float, float]) -> tuple[int, int]:
        cx, cy = cursor
        tx, ty = target
        return (
            int(cx + (tx - cx) * self.smooth),
            int(cy + (ty - cy) * self.smooth),
        )