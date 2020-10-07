tuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]


def last(t):
    return t[-1]


def sort_last(tuples):
    return sorted(tuples, key=last)


print(sort_last(tuples))

