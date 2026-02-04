# test/test_cases.py
import pytest
from src.STUDENT_GRADE_CALCULATOR import calculate_average, determine_grade

def test_calculate_average():
    assert calculate_average([100, 90, 80, 70, 60]) == 80
    assert calculate_average([50, 50, 50, 50, 50]) == 50

def test_calculate_average_invalid():
    
    with pytest.raises(ValueError):
        calculate_average([100, 90])  # Less than 5 marks

def test_determine_grade():
    assert determine_grade(95) == "A+"
    assert determine_grade(80) == "A"
    assert determine_grade(65) == "B"
    assert determine_grade(55) == "C"
    assert determine_grade(40) == "Fail"
