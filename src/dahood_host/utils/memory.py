"""Pointer chain resolution helpers for Da Hood memory reads."""
from __future__ import annotations

from pymem import Pymem


def resolve_pointer_chain(pm: Pymem, base: int, offsets: list[int]) -> int:
    addr = base
    for off in offsets[:-1]:
        addr = pm.read_longlong(addr) + off
    return addr + offsets[-1]


def read_vector3(pm: Pymem, address: int) -> tuple[float, float, float]:
    raw = pm.read_bytes(address, 12)
    import struct

    return struct.unpack("<fff", raw)