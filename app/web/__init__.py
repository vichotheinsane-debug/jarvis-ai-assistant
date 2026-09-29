def test_state_defaults():
    from app.core.state import state

    assert state.status in {"ACTIVE", "LISTENING", "THINKING", "SPEAKING", "NIGHT_MODE", "SUSPENDING", "SUSPENDED", "WAKING", "READY", "OFFLINE"}
    assert isinstance(state.plugins, list)
