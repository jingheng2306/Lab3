import pytest
import Lab2submodule.bmiexercise1 as bmi

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.73, 70) == 0

def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.73, 80) == 1

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.73, 50) == -1