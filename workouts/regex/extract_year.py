import sys
import re

file = "/home/nova/webdev-lessons/python-test/week 3/baby1990.html"


def extract_year(file):
    years = []
    f = open(file, "r")
    text = f.read()

    year_match = re.search(r"Popularity\sin\s(\d\d\d\d)", text)
    if not year_match:
        sys.stderr.write("no year")
        sys.exit(1)
    year = year_match.group(1)
    years.append(year)

    print("the year is ", years)


extract_year(file)

