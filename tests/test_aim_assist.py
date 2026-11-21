from dahood_host.overlay import AimAssist
from dahood_host.overlay.esp_overlay import Box


def test_pick_nearest_within_fov():
    aim = AimAssist(fov=200.0)
    boxes = [
        Box(x=100, y=100, w=20, h=40),
        Box(x=900, y=500, w=20, h=40),
    ]
    picked = aim.pick_target(boxes, cursor=(110, 120))
    assert picked is boxes[0]


def test_no_target_outside_fov():
    aim = AimAssist(fov=5.0)
    boxes = [Box(x=900, y=900, w=10, h=10)]
    assert aim.pick_target(boxes, cursor=(0, 0)) is None