words = ["aba", "xyz", "aa", "x", "bbb", "fsa"]


def match_ends(words):
    count = 0

    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            count += 1
            return count


print(match_ends(words))
