from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("jarvis")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(handler)


def log_event(level: str, message: str, **context: Any) -> None:
    safe_context = {k: v for k, v in context.items() if not isinstance(v, (str)) or "key" not in k.lower() and "token" not in k.lower()}
    if safe_context:
        logger.log(getattr(logging, level.upper(), logging.INFO), "%s | %s", message, safe_context)
    else:
        logger.log(getattr(logging, level.upper(), logging.INFO), message)
