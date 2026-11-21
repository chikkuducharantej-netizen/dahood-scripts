"""Auto-farm plugin — loops Da Hood cash pickup routines."""
from __future__ import annotations

from dahood_host.contracts import HostContext, PluginMeta
from dahood_host.executor_bridge import ExecutorBridge
from dahood_host.scripts.snippets import ANTI_AFK, WALKS_SPEED


LOOP_SCRIPT = WALKS_SPEED + "\n" + ANTI_AFK


class DaHoodAutoFarmPlugin:
    meta = PluginMeta(
        name="da_hood_autofarm",
        version="0.9.1",
        description="Auto-farm cash and anti-AFK loop for Da Hood",
        author="dahood-scripts",
        tags=("farm", "auto", "afk"),
    )

    def __init__(self) -> None:
        self.bridge = ExecutorBridge()
        self._enabled = False

    def on_enable(self) -> None:
        if self.bridge.health():
            self.bridge.execute(LOOP_SCRIPT)
            self._enabled = True

    def on_disable(self) -> None:
        self._enabled = False

    def on_tick(self, ctx: HostContext) -> None:
        return


PLUGIN = DaHoodAutoFarmPlugin