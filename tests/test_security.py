from app.plugins.registry import PluginManager


def test_plugin_registry():
    manager = PluginManager()
    plugins = manager.list_plugins()
    assert any(p["name"] == "weather" for p in plugins)
    assert manager.get("pc") is not None
