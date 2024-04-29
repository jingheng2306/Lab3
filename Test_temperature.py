# Test_Lab2.py

import Lab2submodule # Importing the functions from Lab2.py
import pytest

def test_calc_average_temperature():
    temperatures = [20, 25, 30, 35, 40]
    expected_average = 30.0
    assert Lab2submodule.calc_average_temperature(temperatures) == expected_average

def test_calc_min_max_temperature():
    temperatures = [20, 25, 30, 35, 40]
    expected_min = 20
    expected_max = 40
    assert Lab2submodule.calc_min_max_temperature(temperatures) == [expected_min, expected_max]

def test_calc_median_temperature():
    temperatures = [20, 25, 30, 35, 40]
    expected_median = 30
    assert Lab2submodule.calc_median_temperature(temperatures) == expected_median


