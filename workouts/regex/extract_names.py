import re
import sys

file = "/home/nova/webdev-lessons/python-test/week 3/baby1990.html"


def extract_name(file):
    names = []
    f = open(file, "r")
    text = f.read
    tuples = re.findall(r"<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>", text)

    names_to_rank = {}
    for rank_tuple in tuples:
        (rank, boyname, girlname) = rank_tuple
        if boyname not in names_to_rank:
            names_to_rank[boyname] = rank
        if girlname not in names_to_rank:
            names_to_rank[girlname] = rank

    sorted_names = sorted(names_to_rank.keys())
    for name in sorted_names:
        names.append(names + " " + names_to_rank[name])

    print(names)


extract_name(file)
