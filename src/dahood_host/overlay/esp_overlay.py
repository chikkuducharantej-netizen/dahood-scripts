"""Transparent overlay for ESP boxes drawn from Da Hood player positions."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Box:
    x: int
    y: int
    w: int
    h: int
    label: str = ""


class EspOverlay:
    def __init__(self, width: int = 1920, height: int = 1080) -> None:
        self.width = width
        self.height = height
        self._boxes: list[Box] = []

    def update(self, boxes: list[Box]) -> None:
        self._boxes = [b for b in boxes if self._in_bounds(b)]

    def _in_bounds(self, b: Box) -> bool:
        return 0 <= b.x < self.width and 0 <= b.y < self.height and b.w > 0 and b.h > 0

    def render(self) -> list[Box]:
        # actual drawing happens in the native overlay hook
        return list(self._boxes)

    def clear(self) -> None:
        self._boxes.clear()