
"""Tests for branch coverage of the coffee shop application."""

import pytest

from coffee_shop_order import (
    process_order_batch,
    check_espresso_machine,
)


def test_invalid_orders_branches():
    with pytest.raises(ValueError):
        process_order_batch("invalid", 0.1)

    with pytest.raises(ValueError):
        process_order_batch([], -0.1)


def test_paid_and_unpaid_orders():
    orders = [
        {"paid": True, "size": "small"},
        {"paid": False, "size": "medium"},
    ]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 3.0,
        "status": "COMPLETED",
    }


def test_all_size_branches():
    orders = [
        {"paid": True, "size": "small"},
        {"paid": True, "size": "medium"},
        {"paid": True, "size": "large"},
        {"paid": True, "size": "unknown"},
    ]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 13.5,
        "status": "COMPLETED",
    }


def test_syrup_cost_branches():
    orders = [
        {
            "paid": True,
            "size": "small",
            "customizations": [
                {"type": "syrup", "cost": 1.0}
            ],
        },
        {
            "paid": True,
            "size": "small",
            "customizations": [
                {"type": "syrup", "cost": 2.0}
            ],
        },
    ]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 8.5,
        "status": "COMPLETED",
    }


def test_negative_and_nonnegative_customization_costs():
    orders = [{
        "paid": True,
        "size": "medium",
        "customizations": [
            {"type": "milk", "cost": -1.0},
            {"type": "milk", "cost": 0.5},
        ],
    }]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 5.0,
        "status": "COMPLETED",
    }


def test_allergy_alert_branches():
    orders = [
        {
            "paid": True,
            "size": "small",
            "strict_allergy": False,
            "customizations": [
                {"type": "allergen_alert", "cost": 0.0}
            ],
        },
        {
            "paid": True,
            "size": "large",
            "strict_allergy": True,
            "customizations": [
                {"type": "allergen_alert", "cost": 0.0}
            ],
        },
    ]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 3.0,
        "status": "COMPLETED",
    }


def test_member_and_nonmember_branches():
    orders = [
        {"paid": True, "size": "small", "is_member": True},
        {"paid": True, "size": "small", "is_member": False},
    ]

    result = process_order_batch(orders, 0.0)

    assert result == {
        "total": 5.7,
        "status": "COMPLETED",
    }


def test_audit_and_no_sale_statuses():
    audit_result = process_order_batch(
        [{"paid": True, "size": "unknown"} for _ in range(5)],
        0.1,
    )

    no_sale_result = process_order_batch(
        [{"paid": False, "size": "small"}],
        0.1,
    )

    assert audit_result == {
        "total": 0.0,
        "status": "AUDIT_REJECTED",
    }

    assert no_sale_result == {
        "total": 0.0,
        "status": "NO_SALE",
    }


def test_completed_status_with_tax():
    result = process_order_batch(
        [{"paid": True, "size": "medium"}],
        0.1,
    )

    assert result == {
        "total": 4.95,
        "status": "COMPLETED",
    }


def test_espresso_machine_no_data():
    assert check_espresso_machine([]) == "NO_DATA"


def test_espresso_machine_shutdown_branch():
    assert check_espresso_machine([[97.0, 97.5]]) == "SHUTDOWN"


def test_espresso_machine_optimal_branches():
    assert check_espresso_machine([[95.0, 97.0, 94.0]]) == "OPTIMAL"
    assert check_espresso_machine([[97.0, 95.0, 97.0]]) == "OPTIMAL"
