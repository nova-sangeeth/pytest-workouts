import re

lines = [
    "sure: nova, prename: hello",
    "profession: software dev",
    "surname:Nova, prename: testname, profession:test_profession",
]

for line in lines:
    print(re.split(",* *\w*:", line)[1:])

