from __future__ import annotations

from app.config.settings import settings
from app.core.logger import log_event


class Guardrails:
    @staticmethod
    def sanitize(text: str) -> str:
        blocked = ["api_key", "token", "password", "secret", "Authorization"]
        lowered = text.lower()
        if any(item in lowered for item in blocked):
            raise ValueError("Entrada no segura: contenido sensible detectado.")
        return text.strip()

    @staticmethod
    def protect_prompt(text: str) -> str:
        prompt = text.strip()
        if len(prompt) > 2000:
            raise ValueError("Entrada demasiado larga para procesarse de forma segura.")
        return prompt

    @staticmethod
    def safe_operation(action: str, target: str | None = None) -> bool:
        if action not in settings.allowlist:
            log_event("WARNING", "Blocked disallowed action", action=action, target=target)
            return False
        return True
