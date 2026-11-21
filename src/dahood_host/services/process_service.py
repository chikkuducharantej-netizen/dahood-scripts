"""Attach to the Roblox player process (RobloxPlayerBeta.exe)."""
from __future__ import annotations

from pymem import Pymem
from pymem.exception import ProcessNotFound


class ProcessService:
    PROCESS_NAME = "RobloxPlayerBeta.exe"

    def __init__(self) -> None:
        self._pm: Pymem | None = None

    def attach(self) -> bool:
        try:
            self._pm = Pymem(self.PROCESS_NAME)
            return True
        except ProcessNotFound:
            return False

    @property
    def handle(self):
        return self._pm

    def detach(self) -> None:
        self._pm = None

    def read_bytes(self, address: int, size: int) -> bytes:
        if self._pm is None:
            raise RuntimeError("not attached to Roblox")
        return self._pm.read_bytes(address, size)