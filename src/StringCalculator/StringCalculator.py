def Add(stringinput: str):
    if stringinput == "":
        return 0
    sum = 0
    FirstInput = stringinput.split(sep=',')
    for x in FirstInput:
        sum = sum + int(x)
    return sum
