# working out with methods in classes.


class nova:
    type = "Human"

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def contact(self, phone, email):
        self.phone = phone
        self.email = email


testing = nova.contact(str(12312), "novasangeeth@trex.com", "email")

print(testing.email)

