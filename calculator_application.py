"""Discount calculator used for Lab 6 coverage analysis."""


def calculate_discount(price, is_member):
    """Return the final price after membership and order-value discounts."""
    discount = 0
    if is_member:
        discount = 0.10
    if price > 100:
        discount += 0.05
    return price * (1 - discount)
