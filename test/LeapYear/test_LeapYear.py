from src.LeapYear.LeapYear import LeapYear


def test_LeapYear():
    assert LeapYear(1900) == "lp"


def test_LeapYear2():
    assert LeapYear(1901) == "nlp"
