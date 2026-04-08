class User:
    def __init__(self, name, surname, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.surname = surname
    def get_info(self):
        return f"{self.name} {self.surname} {self.age} {self.email}"
user1 = User("John", "Smith", 21, "jonhsmith9@gmail.com")
user2 = User("Vali", "Alijanov", 22, "valialijonov87@gmail.com")
user3 = User("Hasan", "Olimov", 1999, "hasanolimov9@yahoo.com")

print(user1.get_info())
print(user2.get_info())
print(user3.get_info())

