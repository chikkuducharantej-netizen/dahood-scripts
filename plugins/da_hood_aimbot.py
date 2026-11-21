"""Aim assist plugin — snaps cursor toward nearest Da Hood target."""
from __future__ import annotations

from dahood_host.contracts import HostContext, PluginMeta
from dahood_host.overlay import AimAssist
from dahood_host.overlay.esp_overlay import Box


class DaHoodAimbotPlugin:
    meta = PluginMeta(
        name="da_hood_aimbot",
        version="1.1.3",
        description="Aim assist for Da Hood with configurable FOV and smoothing",
        author="dahood-scripts",
        tags=("aimbot", "aim-assist", "combat"),
    )

    def __init__(self) -> None:
        self.aim = AimAssist(fov=120.0, smooth=0.35)
        self._enabled = False

    def on_enable(self) -> None:
        self._enabled = True

    def on_disable(self) -> None:
        self._enabled = False

    def on_tick(self, ctx: HostContext) -> None:
        if not self._enabled:
            return
        cursor = ctx.extras.get("cursor", (960, 540))
        raw_boxes = ctx.extras.get("boxes", [])
        boxes = [Box(x=b["x"], y=b["y"], w=b["w"], h=b["h"]) for b in raw_boxes]
        target = self.aim.pick_target(boxes, cursor)
        if target:
            tx = target.x + target.w / 2
            ty = target.y + target.h / 2
            ctx.extras["aim_target"] = self.aim.step_towards(cursor, (tx, ty))


PLUGIN = DaHoodAimbotPlugin