from src.StringCalculator.StringCalculator import Add


def test_Firstinput():
    assert Add("") == 0


def test_First_input_4():
    assert Add("4") == 4


def test_one_and_two_input():
    assert Add("1,2") == 3
