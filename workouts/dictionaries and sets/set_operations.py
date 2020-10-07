a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {1, 2, 3, 4, 5, 6, 7, 8, 9}


print("set Operations")

set_union = a.union(b)
print(set_union)

set_intersection = a.intersection(b)
print(set_intersection)

d = a.union(b)

d.intersection(c)

print(d)

print("difference in sets")

diff = a.difference(b)
print(diff)

print("diff in a ")

diff_b = b.difference(a)

print(diff_b)


print("neither a nor b but the intersection")

diff_inter = a.symmetric_difference(b)

print(diff_inter)
