from dahood_host.contracts import PluginBase, PluginMeta
from dahood_host.registry import PluginRegistry


class _Dummy:
    meta = PluginMeta(name="dummy", version="0.0.1")

    def on_enable(self) -> None: ...
    def on_disable(self) -> None: ...
    def on_tick(self, ctx) -> None: ...


def test_register_and_get():
    reg = PluginRegistry()
    reg.register("dummy", _Dummy(), _Dummy.meta)
    assert reg.get("dummy") is not None
    assert len(reg) == 1


def test_missing_returns_none():
    reg = PluginRegistry()
    assert reg.get("nope") is None