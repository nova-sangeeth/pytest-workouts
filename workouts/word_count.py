# print("the wordcount program")


# text = open("/home/nova/webdev-lessons/python-test/workouts/file..txt", "r")

# d = dict()
# # lower casing the whole file and sorting it accordingly
# # def word_count(d, text):
# for line in text:
#     line = line.strip()
#     line = line.lower()
#     words = line.split(" ")
#     for word in words:
#         if word in d:
#             d[word] = d[word] + 1
#         else:
#             d[word] = 1


# for key in list(d.keys()):
#     print(key, ":", d[key])


# ---------------------------------------------------------------


# file_name = "text_needed.txt"


# def build_dict(file_name):
#     f = open(file_name, "rU")
#     words = f.read().split()
#     count = {}

#     for word in words:
#         word = word.lower()
#         if word not in count:
#             count[word] = 1
#         else:
#             count[word] += 1

#     f.close()

#     return count


# def print_words(file_name):
#     dict = build_dict(file_name)

#     for word in sorted(dict.keys()):
#         print(word, dict[word])


# def print_top(file_name):
#     count = build_dict(file_name)
#     i = 0

#     items = sorted(count.items(), key=sort_value, reverse=True)
#     for item in items[:20]:
#         print(item[0] + str(item[1]) + "times")
#         i += 1


import sys

print("The word count Program 2")


#

# Add the whole path to the file.
# filename = "/home/nova/webdev-lessons/python-test/workouts/file..txt"
#   ADDED CONTEXT MANAGER FOR THE FILE.

f = open("/home/nova/webdev-lessons/python-test/workouts/file..txt", "r+")
# f = open


def build_dict(f):
    # using r+ instead of rU read and write.
    # f = open(f, "r+")
    words = f.read().split()
    count = {}
    for word in words:
        word = word.lower()
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    # f.close()

    return count


def print_words(f):
    word_count = build_dict(f)
    words = sorted(word_count.keys())
    for word in words:
        print(word, word_count[word])


print(print_words(f))

