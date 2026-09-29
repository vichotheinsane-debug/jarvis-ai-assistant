from __future__ import annotations

from abc import ABC, abstractmethod

from app.config.settings import settings


class AIProvider(ABC):
    name: str = "base"

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class LocalProvider(AIProvider):
    name = "local"

    def generate(self, prompt: str) -> str:
        return (
            "No tengo un proveedor externo configurado, pero puedo responder con lógica local. "
            "Su solicitud se procesó de forma segura."
        )


class OpenAIProvider(AIProvider):
    name = "openai"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = api_key or settings.openai_api_key
        self.model = model or settings.ai_model

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise RuntimeError("OpenAI no está configurado.")
        return f"[OpenAI:{self.model}] {prompt[:150]}"


class AnthropicProvider(AIProvider):
    name = "anthropic"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = api_key or settings.anthropic_api_key
        self.model = model or settings.ai_model

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise RuntimeError("Anthropic no está configurado.")
        return f"[Anthropic:{self.model}] {prompt[:150]}"


class GoogleProvider(AIProvider):
    name = "google"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = api_key or settings.google_api_key
        self.model = model or settings.ai_model

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise RuntimeError("Google no está configurado.")
        return f"[Google:{self.model}] {prompt[:150]}"


def get_provider() -> AIProvider:
    configured = settings.configured_ai_providers
    if "openai" in configured and settings.openai_api_key:
        return OpenAIProvider()
    if "anthropic" in configured and settings.anthropic_api_key:
        return AnthropicProvider()
    if "google" in configured and settings.google_api_key:
        return GoogleProvider()
    if "custom" in configured and settings.ai_api_key:
        return LocalProvider()
    return LocalProvider()
