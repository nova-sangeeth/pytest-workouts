import os
import re
import sys

filename = "/home/nova/webdev-lessons/python-test/week 3/baby1990.html"


def extract_names(filename):
    names = []
    f = open(filename, "r+")
    text = f.read()

    year_match = re.search(r"Popularity\sin\s(\d\d\d\d)", text)
    if not year_match:
        sys.stderr.write("year not found")
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)
    print(names)
    print(year)

    tuples = re.findall(r"<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>", text)
    # code the ranking of names.
    print(tuples)
    names_to_rank = {}
    for rank_tuple in tuples:
        # unpack the tuple in multiple vars
        (rank, boyname, girlname) = rank_tuple
        if boyname not in names_to_rank:
            names_to_rank[boyname] = rank
        if girlname not in names_to_rank:
            names_to_rank[girlname] = rank
    sorted_names = sorted(names_to_rank.keys())

    for name in sorted_names:
        names.append(name + "" + names_to_rank[name])

    return names


extract_names(filename)
