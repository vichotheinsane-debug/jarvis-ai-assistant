from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CommandResult:
    intent: str
    action: str
    target: str | None = None
    confirmation_required: bool = False
    response: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
