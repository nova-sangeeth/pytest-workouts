# s = "The dinner was not that bad"


# def not_bad(s):
#     a = s.find("not")
#     if a != -1:
#         if s.find("bad") != -1:
#             b = s.find("bad") + 3
#             if a < b:
#                 removetext = s[a:b]
#                 return s.replace(removetext, "good")
#     return s


# print(not_bad(s))


s = "The Movie was not that bad"


def not_bad(s):
    s_not = s.find("not")
    s_bad = s.find("bad")

    if s_bad > s_not:
        s = s.replace(s[s_not : (s_bad + 4)], "good")

    return s


print(not_bad(s))
