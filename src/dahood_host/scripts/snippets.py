"""Reusable Luau snippets for Da Hood automation."""
from __future__ import annotations

WALKS_SPEED = """
local lp = game.Players.LocalPlayer
if lp and lp.Character then
    local hum = lp.Character:FindFirstChildOfClass("Humanoid")
    if hum then hum.WalkSpeed = 60 end
end
"""

TELEPORT_TO = """
local lp = game.Players.LocalPlayer
local target = game.Players:FindFirstChild("{target}")
if lp and target and target.Character and lp.Character then
    lp.Character:PivotTo(target.Character:GetPivot())
end
"""

ANTI_AFK = """
while true do
    local vu = game:GetService("VirtualUser")
    vu:CaptureController()
    vu:ClickButton2(Vector2.new())
    task.wait(30)
end
"""


def teleport_script(target_name: str) -> str:
    return TELEPORT_TO.format(target=target_name)