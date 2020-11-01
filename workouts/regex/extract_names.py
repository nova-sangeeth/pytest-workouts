import re
import sys

file = "/home/nova/webdev-lessons/python-test/week 3/baby1990.html"


def extract_name(file):
    names = []
    f = open(file, "r")
    text = f.read()
    tuples = re.findall(r"<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>", text)
    print(tuples)


extract_name(file)
