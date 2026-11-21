# Writing a DaHood Script Plugin

Every plugin file lives in `plugins/` and exports a `PLUGIN` symbol:

```python
from dahood_host.contracts import HostContext, PluginMeta

class MyPlugin:
    meta = PluginMeta(
        name="my_plugin",
        version="0.1.0",
        description="does a thing",
        tags=("esp",),
    )
    def on_enable(self) -> None: ...
    def on_disable(self) -> None: ...
    def on_tick(self, ctx: HostContext) -> None: ...

PLUGIN = MyPlugin
```

The host auto-loads any `*.py` file in `plugins/` (files starting with `_` are skipped).

## Available context

- `ctx.process_handle` — attached `Pymem` handle (or `None`)
- `ctx.place_id`, `ctx.player_name`
- `ctx.extras` — shared dict used to pass player tables, cursor, aim target

## Overlay primitives

`dahood_host.overlay.EspOverlay` and `AimAssist` provide the drawing/aim math.