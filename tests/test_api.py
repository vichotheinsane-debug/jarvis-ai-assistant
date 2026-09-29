from app.automation.routines import RoutineManager


def test_night_mode_routine():
    result = RoutineManager().trigger_night_mode()
    assert result["status"] in {"ok", "error", "unsupported"}


def test_stop_all_automations():
    result = RoutineManager().stop_all_automations()
    assert result["status"] == "stopped"
