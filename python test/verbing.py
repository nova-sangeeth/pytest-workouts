a = "roting"


def verbing(a):
    if len(a) > 3 and a[-3:] == "ing":
        a += "ly"
    else:
        a += "ing"
    return a


print(verbing(a))
