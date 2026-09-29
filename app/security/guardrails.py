from __future__ import annotations

from app.config.settings import settings


class PermissionError(RuntimeError):
    pass


class PermissionChecker:
    def __init__(self, allowlist: list[str] | None = None, dangerous: list[str] | None = None):
        self.allowlist = allowlist or settings.allowlist
        self.dangerous = dangerous or settings.dangerous

    def check(self, action: str) -> bool:
        if action not in self.allowlist:
            return False
        return True

    def requires_confirmation(self, action: str) -> bool:
        return action in self.dangerous

    def validate(self, action: str) -> None:
        if not self.check(action):
            raise PermissionError(f"No tengo permisos suficientes para realizar la acción '{action}'.")
