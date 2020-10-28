# basics for clases


class nova:
    type = "Human"

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


testing = nova("nova", 22, "mount road")

print(testing.name)
