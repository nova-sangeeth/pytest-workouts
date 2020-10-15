print("Checking out enumeration with lists.")


colors = ["red", "blue", "green", "black", "violet", "yellow", "cyan"]

# with tuples
for i in enumerate(colors):
    print(i)
# without tuples.

for a, b in enumerate(colors):
    print(a, b)
