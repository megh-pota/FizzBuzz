import pytest

from src.FizzBuzz import fizzbuzz


def test_check_input_3():
    assert fizzbuzz(3) == "Fizz"

def test_check_input_5():
    assert fizzbuzz(5) == "Buzz"