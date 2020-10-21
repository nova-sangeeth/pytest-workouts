import re

print("matching using regular Expressions.")


a = "Hello There, I am a dog !!!"


match_word = re.match(r"There", a, re.M | re.I)

if match_word:
    print("It is a match")
else:
    print("No match.")

