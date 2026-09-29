from app.commands.intent import IntentRouter


def test_open_application_intent():
    result = IntentRouter().route("Señor, abre Roblox")
    assert result.intent == "open_application"
    assert result.action == "open_application"
    assert "roblox" in (result.target or "")


def test_night_mode_intent():
    result = IntentRouter().route("Jarvis, buenas noches")
    assert result.intent == "night_mode"
    assert result.action == "suspend"


def test_help_intent():
    result = IntentRouter().route("¿Qué puedes hacer?")
    assert result.intent == "help"
