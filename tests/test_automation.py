import pytest

from app.security.guardrails import Guardrails


def test_sanitize_rejects_sensitive_strings():
    with pytest.raises(ValueError):
        Guardrails.sanitize("api_key=123")


def test_safe_operation_blocks_unknown_action():
    assert Guardrails.safe_operation("unknown_action") is False
