import re

"""
adding yo yo after each @ symbol using regular expressions.
"""
a = " nova@google.com, test main@abr@.com world main"

test = re.sub(r"([\w\.-]+)@([\w\.-]+)", r"\1@yo-yo-dyne.com", a)

print(test)
