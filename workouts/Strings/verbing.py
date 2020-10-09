# a = "do"


# def verbing(a):
#     if len(a) >= 3 and a[-3:] == "ing":
#         a += "ly"
#     else:
#         a += "ing"
#     return a


# print(verbing(a))


# a = "runing"


# def verbing(a):
#     if len(a) <= 3:
#         return a
#     elif a[-3] == "ing":
#         a += "ly"
#     else:
#         a += "ing"
#     return a


# print(verbing(a))


def verbing(s):
    if len(s) >= 2:
        if s[-3:] == "ing":
            s += "ly"
        else:
            s += "ing"
        return s
