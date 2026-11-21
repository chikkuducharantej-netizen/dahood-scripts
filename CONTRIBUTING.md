# Contributing to dahood-scripts

Thanks for considering a contribution to **dahood-scripts** (Da Hood Roblox Script).

## Scope

- Plugin host (`src/dahood_host/`)
- Bundled plugins (`plugins/`)
- Executor bridge + Luau snippets

## Rules

1. **For educational and personal use only.** Do not submit anything that
   targets other players' accounts or violates Roblox ToS beyond what the
   community already expects of script tools.
2. Every new plugin must expose a `PLUGIN` symbol and a valid `PluginMeta`.
3. Keep `on_tick` fast — it runs on the host's main loop.
4. Add a test under `tests/` if you touch `overlay/`, `registry.py`, or `loader.py`.
5. Run `pytest` and `ruff check src plugins` before opening a PR.

## Commit style

`area: short summary` — e.g. `overlay: fix esp box clipping at screen edges`.

## Reporting issues

Use the issue template with: Python version, Roblox version, executor name,
and the plugin that misbehaved.