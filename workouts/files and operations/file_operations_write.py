file_name = open(
    "/home/nova/webdev-lessons/python-test/workouts/files and operations/test.txt", "w+"
)
dict = {"a": "nova", "b": "john", "c": "harp"}

# reading a file and writing its content to another.
file_name_2 = open(
    "/home/nova/webdev-lessons/python-test/workouts/files and operations/test.txt"
)
for x in dict:

    file_name.write(str(dict))
file_name.close()
