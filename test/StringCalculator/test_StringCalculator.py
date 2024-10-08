import pytest

from src.StringCalculator.StringCalculator import Add


def test_Firstinput():
    assert Add("") == 0


def test_First_input_4():
    assert Add("4") == 4


def test_one_and_two_input():
    assert Add("1,2") == 3


def test_one_to_nine_input():
    assert Add("1,2,3,4,5,6,7,8,9") == 45


def test_nagative_and_positive_input():
    assert Add("-1,0,1") == 0


def test_accept_newline_as_delimiter():
    assert Add("1\n2,3") == 6


def test_accept_custurm_sep():
    assert Add("//;\n12") == 3


def test_handle_neg_num():
    with pytest.raises(Exception) as exe:
        Add("1,-2,-3")
    assert exe.value


def test_accept_less_than_1000():
    assert Add("1001,2") == 2
