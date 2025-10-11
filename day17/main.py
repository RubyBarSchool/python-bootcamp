class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age



user_1 = User("truong", 20)

print(user_1.name)
print(user_1.age)
print(user_1.__dict__)