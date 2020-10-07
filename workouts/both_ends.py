s = "string"


def both_sides(s):
    if len(s) <= 2:
        return ""

    return s[0:2] + s[-2:]


print(both_sides(s))

