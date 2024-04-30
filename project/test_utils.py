from utils import is_estring, calculate_calories, kilograms_lost
import pytest
from pytest import approx




def test_is_estring():
    assert is_estring("s") == True
    assert is_estring(22) == False
    assert is_estring(33.4) == False
    assert is_estring("22") == True
    
    
def test_calculate_calories():
    assert calculate_calories(0, 0, "LB") == False
    assert calculate_calories(2, 45.2, "KG") == approx(87.69, abs=0.1)
    assert calculate_calories(1.5, 120, "LB") == approx(79.20, abs=0.1)
    assert isinstance(calculate_calories("d", "df", "LB"), TypeError)
    assert str(calculate_calories("d", "df", "LB")) == "Body weight and distance must be numbers"


def test_kilograms_lost():
    
    assert kilograms_lost(1000) == 7
    assert kilograms_lost("abc") == "Please, enter a valid input"
    assert kilograms_lost("text") == "Please, enter a valid input"
    assert kilograms_lost(0) == "Calories burned must be greater than 0"
    assert kilograms_lost(-100) == "Calories burned must be greater than 0"

    
pytest.main(["-v", "--tb=line", "-rN", "project/test_utils.py"])
