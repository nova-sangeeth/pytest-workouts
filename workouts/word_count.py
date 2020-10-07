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
import sys

print("The word count Program 2")


def sort_value(item):
    return item[-1]


# Add the whole path to the file.
filename = "/home/nova/webdev-lessons/python-test/workouts/file..txt"


def build_dict(filename):
    # using r+ instead of rU read and write.
    f = open(filename, "r+")
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


print(build_dict(filename))
