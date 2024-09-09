def Add(stringinput: str):
    if stringinput == "":
        return 0

    num = []
    stringinput = stringinput.replace('\n', ',')
    FirstInput = stringinput.split(sep=',')
    num = [int(y) for y in FirstInput if y and int(y) <= 1000]
    neg = [y2 for y2 in num if y2 < 0]
    if neg:
        raise Exception("negetive number not allowed")

    ans = sum(num)
    return ans
