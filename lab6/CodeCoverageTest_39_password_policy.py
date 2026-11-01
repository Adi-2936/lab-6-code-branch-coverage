"""Tests designed to exceed 90% statement coverage in password_policy.py."""

from password_policy import check_password, strength, suggest_fix


def test_valid_password_and_good_strength():
    assert check_password("Abcdef1!") == []
    assert strength("Abcdef1!") == "good"


def test_short_password_and_suggestion():
    issues = check_password("Ab1!")
    assert "too short" in issues
    assert suggest_fix(issues) == "add more characters"


def test_common_password_and_suggestion():
    issues = check_password("password")
    assert "common" in issues
    assert suggest_fix(issues) == "avoid common passwords"


def test_missing_character_classes():
    assert "no lowercase" in check_password("ABCDEFG1!")
    assert "no uppercase" in check_password("abcdefg1!")
    assert "no digit" in check_password("Abcdefgh!")
    assert "no special" in check_password("Abcdefg1")


def test_weak_and_very_weak_strengths():
    assert strength("abcdefg1!") == "weak"
    assert strength("abc") == "very weak"


def test_no_character_class_suggestion():
    assert suggest_fix(["no uppercase"]) == "add uppercase"
