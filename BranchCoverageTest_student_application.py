"""Branch-coverage test suite for the discount calculator."""

import pytest

from calculator_application import calculate_discount


@pytest.mark.parametrize(
    ("price", "is_member", "expected"),
    [
        pytest.param(150, True, 127.5, id="member-expensive"),
        pytest.param(100, True, 90.0, id="member-boundary"),
        pytest.param(150, False, 142.5, id="nonmember-expensive"),
        pytest.param(100, False, 100.0, id="nonmember-boundary"),
    ],
)
def test_all_decision_outcomes(price, is_member, expected):
    """Cover True and False outcomes for both independent decisions."""
    assert calculate_discount(price, is_member) == expected
