# DaHood Scripts — Architecture

The host is a **plugin host** for Da Hood Roblox script extensions.

```
src/dahood_host/
├── cli.py                 entry point
├── loader.py              dynamic plugin loader
├── registry.py            plugin registry
├── contracts.py           shared PluginBase / PluginMeta
├── executor_bridge.py     HTTP bridge to the Roblox executor
├── overlay/               ESP + aim assist drawing primitives
├── services/              process attach + config
├── models/                Player / Session state
├── scripts/               bundled Luau snippets
└── utils/                 memory helpers + logging
plugins/                   drop-in plugin modules (PLUGIN symbol)
```

## Lifecycle

1. `cli.py` builds a `PluginRegistry`.
2. `PluginLoader.load_all()` imports every `plugins/*.py` and reads its `PLUGIN`.
3. Each plugin's `on_enable()` is invoked by the host tick loop.
4. `on_tick(ctx)` receives a `HostContext` with the current player table + cursor.

## Executor contract

The executor (Synapse-style) exposes:

- `POST /execute` — run a Luau string
- `POST /dump` — dump strings / offsets
- `GET  /health`

Configure endpoint via `config.local.toml → executor_endpoint`.