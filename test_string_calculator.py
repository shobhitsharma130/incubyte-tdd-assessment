import pytest
from string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_value():
    assert add("5") == 5

def test_two_numbers():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3,4") == 10

def test_newline_and_comma_delimiters():
    assert add("1\n2,3") == 6

def test_custom_delimiter_single_char():
    assert add("//;\n1;2") == 3

def test_negative_numbers_raise_exception():
    with pytest.raises(ValueError, match="Negatives not allowed:"):
        add("1,-2,3,-5")

def test_numbers_bigger_than_1000_are_ignored():
    assert add("2,1001") == 2
    assert add("1000,3") == 1003

def test_delimiters_of_any_length():
    assert add("//[***]\n1***2***3") == 6
    assert add("//[abc]\n4abc5abc6") == 15