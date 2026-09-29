from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SystemState:
    status: str = "ACTIVE"
    voice_state: str = "IDLE"
    microphone_state: str = "ACTIVE"
    plugins: list[str] = field(default_factory=list)
    automations: list[str] = field(default_factory=list)
    connected_devices: list[str] = field(default_factory=list)
    memory_enabled: bool = True
    night_mode: bool = False
    suspend_ready: bool = False
    last_command: str = ""
    last_response: str = ""


state = SystemState()
