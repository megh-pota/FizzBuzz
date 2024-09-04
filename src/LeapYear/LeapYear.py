def LeapYear(self):
    if self % 4 == 0 and self % 100 == 0:
        return "lp"
    elif self % 4 == 0:
        return "lp"
    elif self % 100 == 0:
        return "lp"
    else:
        return "nlp"
