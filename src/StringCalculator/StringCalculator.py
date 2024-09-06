def Add(stringinput: str):
    if stringinput == "":
        return 0
    else:
        sum = 0
        FirstInput = stringinput.split(sep=',')
        for x in FirstInput:
            sum = sum + int(x)
        return sum


Add("1,2")
