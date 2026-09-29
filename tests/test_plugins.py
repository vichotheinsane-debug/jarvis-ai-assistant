from app.memory.memory import MemoryStore
from app.database.db import init_db


def test_memory_roundtrip():
    db = init_db()
    store = MemoryStore(db)
    store.set("user_name", "Vicho")
    assert store.get("user_name") == "Vicho"
    store.delete("user_name")
    assert store.get("user_name") is None
