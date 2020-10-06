a = "abcde"
b = "xyz"


# def front_back(a, b):
#     if len(a) and len(b) % 2 == 0:

#         print(a[0:3] + " " + b[-3:])
#         print("this one is even")

#     else:

#         print("Add another to the front.")


# print(front_back(a, b))


# def front_back(a, b):
#     if len(a) and len(b) % 2 == 0:
#         first_part
#         second_part
#         third_part
#         fourth_part


# added // for the division part cuz this one outputs a float
def front_back(a, b):
    len_a, len_b = (len(a) + 1) // 2, (len(b) + 1) // 2
    return a[:len_a] + b[:len_b] + a[len_a:] + b[len_b:]


print(front_back(a, b))


# METHOD n


# def front_back(a, b):
#     a_string = len(a) / 2 + (len(a) % 2)
#     b_string = len(b) / 2 + (len(b) % 2)

#     return a[:a_string] + b[:b_string] + a[a_string:] + b[b_string:]


# print(front_back(a, b))

