"""Line-coverage test suite for the discount calculator."""

from calculator_application import calculate_discount


def test_member_expensive_item_executes_every_statement():
    """Exercise both discount statements to reach complete line coverage."""
    assert calculate_discount(150, True) == 127.5
