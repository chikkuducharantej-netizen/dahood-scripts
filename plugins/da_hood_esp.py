"""ESP plugin — draws boxes around Da Hood players via the overlay."""
from __future__ import annotations

from dahood_host.contracts import HostContext, PluginMeta
from dahood_host.overlay import EspOverlay
from dahood_host.overlay.esp_overlay import Box


class DaHoodEspPlugin:
    meta = PluginMeta(
        name="da_hood_esp",
        version="1.2.0",
        description="Wallhack / ESP boxes for Da Hood players",
        author="dahood-scripts",
        tags=("esp", "wallhack", "overlay"),
    )

    def __init__(self) -> None:
        self.overlay = EspOverlay()
        self._enabled = False

    def on_enable(self) -> None:
        self._enabled = True

    def on_disable(self) -> None:
        self._enabled = False
        self.overlay.clear()

    def on_tick(self, ctx: HostContext) -> None:
        if not self._enabled:
            return
        players = ctx.extras.get("players", [])
        boxes = [
            Box(x=p["x"], y=p["y"], w=p["w"], h=p["h"], label=p.get("name", ""))
            for p in players
        ]
        self.overlay.update(boxes)


PLUGIN = DaHoodEspPlugin