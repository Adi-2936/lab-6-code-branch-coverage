"""Tests covering every decision outcome in password_policy.py."""

import pytest

from password_policy import check_password, strength, suggest_fix


@pytest.mark.parametrize(
    ("password", "expected_issue"),
    [
        pytest.param("Ab1!", "too short", id="short"),
        pytest.param("A" * 65 + "a1!", "too long", id="long"),
        pytest.param("password", "common", id="common"),
        pytest.param("abcdefg1!", "no uppercase", id="no-uppercase"),
        pytest.param("ABCDEFG1!", "no lowercase", id="no-lowercase"),
        pytest.param("Abcdefgh!", "no digit", id="no-digit"),
        pytest.param("Abcdefg1", "no special", id="no-special"),
    ],
)
def test_each_policy_violation(password, expected_issue):
    assert expected_issue in check_password(password)


def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


@pytest.mark.parametrize(
    ("password", "expected_strength"),
    [
        pytest.param("Abcdefghijklm1!", "strong", id="strong"),
        pytest.param("Abcdef1!", "good", id="good"),
        pytest.param("abcdefg1!", "weak", id="weak"),
        pytest.param("abc", "very weak", id="very-weak"),
    ],
)
def test_every_strength_outcome(password, expected_strength):
    assert strength(password) == expected_strength


@pytest.mark.parametrize(
    ("issues", "expected"),
    [
        pytest.param([], "none needed", id="none"),
        pytest.param(["too short"], "add more characters", id="short"),
        pytest.param(["common"], "avoid common passwords", id="common"),
        pytest.param(["no uppercase"], "add uppercase", id="missing-class"),
        pytest.param(["too long"], "shorten it", id="fallback"),
    ],
)
def test_every_suggestion_outcome(issues, expected):
    assert suggest_fix(issues) == expected
