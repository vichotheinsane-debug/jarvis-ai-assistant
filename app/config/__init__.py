from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")


class Settings(BaseSettings):
    app_env: str = "development"
    api_key: str = "change-me"
    jarvis_name: str = "Jarvis"
    user_name: str = "Vicho"
    user_display_name: str = "señor Vicho"
    ai_api_key: str = ""
    ai_model: str = "gpt-4o-mini"
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    google_api_key: str = ""
    elevenlabs_api_key: str = ""
    weather_api_key: str = ""
    home_assistant_url: str = ""
    home_assistant_token: str = ""
    voice_provider: str = "local"
    voice_id: str = ""
    voice_language: str = "es-ES"
    wake_word: str = "Hey Nexus"
    wake_word_enabled: bool = False
    microphone_enabled: bool = True
    db_path: str = "data/jarvis.db"
    log_level: str = "INFO"
    system_name: str = "local-pc"
    allowlist_actions: str = "open_application,close_application,open_url,open_file,open_folder,volume_control,media_control,system_information,shutdown,restart,suspend"
    dangerous_actions: str = "shutdown,restart,delete_files"
    night_mode_enabled: bool = True
    night_mode_suspend: bool = True

    model_config = {"env_file": ".env", "case_sensitive": False}

    @property
    def configured_ai_providers(self) -> list[str]:
        providers: list[str] = []
        if self.openai_api_key:
            providers.append("openai")
        if self.anthropic_api_key:
            providers.append("anthropic")
        if self.google_api_key:
            providers.append("google")
        if self.ai_api_key:
            providers.append("custom")
        if not providers:
            providers.append("local")
        return providers

    @property
    def allowlist(self) -> list[str]:
        return [item.strip() for item in self.allowlist_actions.split(",") if item.strip()]

    @property
    def dangerous(self) -> list[str]:
        return [item.strip() for item in self.dangerous_actions.split(",") if item.strip()]


settings = Settings()
