import re

a = "main, google-hello@gmail.com, hellow@yahoo.com, tyron, main@gg.com, kk, og."

print("regular expressions -2 for email extractions.")


def reg_email(a):
    emails = re.findall(r"[\w\.-]+@[\w\.-]+", a)

    for email in emails:
        print(email)


reg_email(a)
