words = ["xaa", "xzz", "axx", "bbb", "ccc"]


def front_x(words):
    x_words = []
    a_words = []

    for word in words:
        if word.startswith("x"):
            x_words.append(word)
        else:
            a_words.append(word)

    return x_words + a_words


print(front_x(words))
