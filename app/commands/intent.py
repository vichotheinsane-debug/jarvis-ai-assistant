from __future__ import annotations

import json
from typing import Any

from app.database.db import DatabaseManager


class MemoryStore:
    def __init__(self, db: DatabaseManager | None = None):
        self.db = db or DatabaseManager()

    def set(self, key: str, value: Any) -> None:
        with self.db.connection() as conn:
            conn.execute(
                "INSERT INTO memory_items(key, value) VALUES(?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                (key, json.dumps(value, ensure_ascii=False)),
            )

    def get(self, key: str, default: Any = None) -> Any:
        with self.db.connection() as conn:
            row = conn.execute("SELECT value FROM memory_items WHERE key = ?", (key,)).fetchone()
            if row is None:
                return default
            return json.loads(row["value"])

    def delete(self, key: str) -> None:
        with self.db.connection() as conn:
            conn.execute("DELETE FROM memory_items WHERE key = ?", (key,))

    def list(self) -> dict[str, Any]:
        with self.db.connection() as conn:
            rows = conn.execute("SELECT key, value FROM memory_items ORDER BY key").fetchall()
        return {row["key"]: json.loads(row["value"]) for row in rows}

    def append_history(self, text: str, intent: str | None = None, status: str = "OK") -> None:
        with self.db.connection() as conn:
            conn.execute(
                "INSERT INTO command_history(text, intent, status) VALUES(?,?,?)",
                (text, intent, status),
            )

    def get_history(self) -> list[dict[str, str]]:
        with self.db.connection() as conn:
            rows = conn.execute(
                "SELECT text, intent, status, created_at FROM command_history ORDER BY id DESC LIMIT 50"
            ).fetchall()
        return [dict(row) for row in rows]
