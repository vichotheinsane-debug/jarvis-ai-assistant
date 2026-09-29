from __future__ import annotations

from abc import ABC, abstractmethod


class STTProvider(ABC):
    name = "base"

    @abstractmethod
    def listen(self) -> str:
        raise NotImplementedError


class TTSProvider(ABC):
    name = "base"

    @abstractmethod
    def speak(self, text: str) -> None:
        raise NotImplementedError


class LocalSTT(STTProvider):
    name = "local"

    def listen(self) -> str:
        return ""


class LocalTTS(TTSProvider):
    name = "local"

    def speak(self, text: str) -> None:
        return None


class ElevenLabsTTS(TTSProvider):
    name = "elevenlabs"

    def speak(self, text: str) -> None:
        return None
