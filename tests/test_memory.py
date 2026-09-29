from app.security.permissions import PermissionChecker


def test_allowed_action():
    checker = PermissionChecker(["open_application", "volume_control"], ["shutdown"])
    assert checker.check("open_application") is True


def test_dangerous_requires_confirmation():
    checker = PermissionChecker(["shutdown"], ["shutdown"])
    assert checker.requires_confirmation("shutdown") is True
