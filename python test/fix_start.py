s = "babble"


def fix_start(s):
    char = s[0]
    s = s.replace(char, "*")
    s = char + s[1:]

    return s


print(fix_start(s))

