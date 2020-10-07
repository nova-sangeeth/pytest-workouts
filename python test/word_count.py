import sys

# from .
def sort_value(item):
    return item[-1]


file_name = "text_needed.txt"


def build_dict(file_name):
    f = open(file_name, "rU")
    words = f.read().split()
    count = {}

    for word in words:
        word = word.lower()
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    f.close()

    return count


def print_words(file_name):
    dict = build_dict(file_name)

    for word in sorted(dict.keys()):
        print(word, dict[word])


def print_top(file_name):
    count = build_dict(file_name)
    i = 0

    items = sorted(count.items(), key=sort_value, reverse=True)
    for item in items[:20]:
        print(item[0] + str(item[1]) + "times")
        i += 1
