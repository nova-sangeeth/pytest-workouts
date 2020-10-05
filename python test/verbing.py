# a = "roting"


# def verbing(a):
#     if len(a) < 3 and a[-3:] == "ing":
#         return a + "ly"
#     else:
#         return a + "ing"


# print(verbing(a))
a = "roting"


def verbing(a):
    if len(a) > 3 and a[-3:] == "ing":
        a += "ly"
    else:
        a += "ing"
    return a


print(verbing(a))
