import re

lines = ["sure: nova, prename: hello", "profession: software dev"]

for line in lines:
    print(re.split(",* *\w*:", line)[1:])

