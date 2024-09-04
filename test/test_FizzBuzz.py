from src.FizzBuzz import fizzbuzz


def test_check_input_3():
    assert fizzbuzz(3) == "Fizz"


def test_check_input_5():
    assert fizzbuzz(5) == "Buzz"


def test_check_input_6():
    assert fizzbuzz(6) == "Fizz"


def test_check_input_10():
    assert fizzbuzz(10) == "Buzz"


def test_check_input_15():
    assert fizzbuzz(15) == "FizzBuzz"


def test_check_input_1():
    assert fizzbuzz(1) == "1"
