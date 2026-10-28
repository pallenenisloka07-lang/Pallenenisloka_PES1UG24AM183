"""Manage energy meter readings, tariff bills, and usage spikes."""

import json
from datetime import datetime
from pathlib import Path

RATE_TIER_1 = 3.5
RATE_TIER_2 = 5.0
RATE_TIER_3 = 7.5
SPIKE_LIMIT = 500
DEFAULT_DATA_FILE = "meters.json"


def record_reading(meters, meter_id, units, history=None):
    """Record a meter reading and update cumulative usage."""
    if units < 0:
        raise ValueError("Energy units cannot be negative.")

    if history is None:
        history = []

    history.append((meter_id, units, str(datetime.now())))
    meters[meter_id] = meters.get(meter_id, 0) + units
    return history


def compute_bill(meters, meter_id, tier_rates):
    """Calculate a progressive energy bill for a meter."""
    if meter_id not in meters:
        raise KeyError(f"Unknown meter: {meter_id}")

    units = meters[meter_id]

    if units <= 100:
        return units * tier_rates[0]

    if units <= 300:
        return (
            100 * tier_rates[0]
            + (units - 100) * tier_rates[1]
        )

    return (
        100 * tier_rates[0]
        + 200 * tier_rates[1]
        + (units - 300) * tier_rates[2]
    )


def raise_rates(tier_rates, percent):
    """Return tariff rates increased by the specified percentage."""
    if percent < 0:
        raise ValueError("Rate increase cannot be negative.")

    multiplier = 1 + percent / 100
    return [rate * multiplier for rate in tier_rates]


def flag_spikes(meters):
    """Return meter IDs whose cumulative usage exceeds the limit."""
    return [
        meter_id
        for meter_id, units in meters.items()
        if units > SPIKE_LIMIT
    ]


def load_meter_data(file=DEFAULT_DATA_FILE):
    """Load meter readings from JSON, or return an empty dictionary."""
    try:
        with Path(file).open(encoding="utf-8") as data_file:
            data = json.load(data_file)

        if not isinstance(data, dict):
            raise ValueError("Meter data must be a JSON object.")

        if any(
            not isinstance(meter_id, str)
            or isinstance(units, bool)
            or not isinstance(units, (int, float))
            or units < 0
            for meter_id, units in data.items()
        ):
            raise ValueError("Invalid meter data in JSON file.")

        return data

    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as error:
        raise ValueError("Meter data file contains invalid JSON.") from error


def save_meter_data(meters, file=DEFAULT_DATA_FILE):
    """Save meter readings to a JSON file."""
    with Path(file).open("w", encoding="utf-8") as data_file:
        json.dump(meters, data_file, indent=4)


def main():
    """Run the energy tariff demonstration."""
    meters = {}
    history = []

    record_reading(meters, "M-01", 120, history)
    record_reading(meters, "M-02", 640, history)
    record_reading(meters, "M-03", 50, history)

    print("Readings stored so far:", len(history))

    rates = raise_rates(
        [RATE_TIER_1, RATE_TIER_2, RATE_TIER_3],
        10,
    )

    print(f"Bill M-01: {compute_bill(meters, 'M-01', rates):.2f}")
    print(f"Bill M-03: {compute_bill(meters, 'M-03', rates):.2f}")
    print("Spikes:", flag_spikes(meters))

    adjustment_text = input(
        "Extra units for M-01 (Enter for 0): "
    ).strip()

    try:
        adjustment = float(adjustment_text) if adjustment_text else 0.0

        if adjustment < 0:
            raise ValueError("Extra units cannot be negative.")

        record_reading(meters, "M-01", adjustment, history)

    except ValueError as error:
        print(f"Invalid adjustment: {error}")
        return

    save_meter_data(meters)
    loaded_meters = load_meter_data()

    print(
        "Bill M-01 after reload: "
        f"{compute_bill(loaded_meters, 'M-01', rates):.2f}"
    )


if __name__ == "__main__":
    main()
