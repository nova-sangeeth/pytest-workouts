import re

email = 'dog dog-qewrtyg@ggy.com'

match = re.search(r'\w+@\w+' , email)
if match: 
    print(match.group())