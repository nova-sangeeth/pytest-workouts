import re

email = 'dog dog-qewrtyg@ggy.com' 

match = re.search(r'\w+@\w+' , email)
if match: 
    print(match.group())

email_2 = "main good helloworld@gmail.com ee"

def reg_main(email_2):
    match = re.search(r'\w+@\w+', email_2)
    if match:
        print(match.group())


reg_main(email_2)    