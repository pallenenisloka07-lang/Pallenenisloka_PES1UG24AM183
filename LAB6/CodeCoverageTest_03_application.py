
"""Tests for code coverage of the coffee shop application."""

import pytest

from coffee_shop_order import (
    process_order_batch,
    check_espresso_machine,
)


def test_invalid_orders_and_tax():
    with pytest.raises(ValueError):
        process_order_batch("not a list", 0.1)

    with pytest.raises(ValueError):
        process_order_batch([], -0.1)


def test_paid_orders_with_all_sizes():
    orders = [
        {"paid": True, "size": "small"},
        {"paid": True, "size": "medium"},
        {"paid": True, "size": "large"},
    ]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 13.5,
        "status": "COMPLETED",
    }


def test_unpaid_and_unknown_size_orders():
    orders = [
        {"paid": False, "size": "medium"},
        {"paid": True, "size": "extra-large"},
    ]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 0.0,
        "status": "NO_SALE",
    }


def test_customizations_and_member_discount():
    orders = [{
        "paid": True,
        "size": "medium",
        "is_member": True,
        "customizations": [
            {"type": "syrup", "cost": 2.0},
            {"type": "milk", "cost": 0.5},
        ],
    }]

    result = process_order_batch(orders, 0.1)

    assert result == {
        "total": 6.44,
        "status": "COMPLETED",
    }


def test_negative_customization_cost():
    orders = [{
        "paid": True,
        "size": "small",
        "customizations": [
            {"type": "syrup", "cost": -1.0}
        ],
    }]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 3.0,
        "status": "COMPLETED",
    }


def test_allergy_alert_without_strict_mode():
    orders = [{
        "paid": True,
        "size": "small",
        "strict_allergy": False,
        "customizations": [
            {"type": "allergen_alert", "cost": 0.0}
        ],
    }]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 3.0,
        "status": "COMPLETED",
    }


def test_strict_allergy_rejects_item():
    orders = [{
        "paid": True,
        "size": "large",
        "strict_allergy": True,
        "customizations": [
            {"type": "allergen_alert", "cost": 0.0}
        ],
    }]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 0.0,
        "status": "NO_SALE",
    }


def test_audit_rejected_after_many_rejections():
    orders = [
        {"paid": True, "size": "unknown"}
        for _ in range(5)
    ]

    result = process_order_batch(orders, 0.1)

    assert result == {
        "total": 0.0,
        "status": "AUDIT_REJECTED",
    }


def test_espresso_machine_no_data():
    assert check_espresso_machine([]) == "NO_DATA"


def test_espresso_machine_shutdown():
    assert check_espresso_machine([[97.0, 97.5]]) == "SHUTDOWN"


def test_espresso_machine_optimal():
    assert check_espresso_machine(
        [[95.0, 97.0, 94.0]]
    ) == "OPTIMAL"
