# test_price_info.py

import price_info
import pytest

def test_total_cost_shopping():
    expected_total_cost = 65.95  # Calculated manually based on the provided price_list and quantity_list
    assert price_info.total_cost_shopping() == expected_total_cost

def test_cost_of_fruit():
    fruit = 'apple'
    quantity = 5
    expected_cost = 1.20 * 5  # Calculated manually based on the provided price_list
    assert price_info.cost_of_fruits(fruit, quantity) == expected_cost
