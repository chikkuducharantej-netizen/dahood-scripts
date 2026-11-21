"""Command-line entry point for the DaHood script host."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rich.console import Console

from .loader import PluginLoader
from .registry import PluginRegistry

console = Console()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dahood", description="Da Hood Roblox Script host")
    p.add_argument("--plugins", default="plugins", help="plugin directory")
    p.add_argument("--list", action="store_true", help="list loaded plugins")
    p.add_argument("--run", metavar="NAME", help="run a single plugin by name")
    p.add_argument("--config", default="config.local.toml", help="config file path")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    registry = PluginRegistry()
    loader = PluginLoader(Path(args.plugins))
    loader.load_all(registry)

    if args.list:
        for name, meta in registry.items():
            console.print(f"[cyan]{name}[/cyan] v{meta.version} — {meta.description}")
        return 0

    if args.run:
        plugin = registry.get(args.run)
        if not plugin:
            console.print(f"[red]plugin not found:[/red] {args.run}")
            return 2
        plugin.on_enable()
        console.print(f"[green]enabled[/green] {args.run}")
        return 0

    console.print("[yellow]no action specified; use --list or --run[/yellow]")
    return 1


if __name__ == "__main__":
    sys.exit(main())