class Fan:
    def __init__(self, matematika):
        self.matematika = matematika

class Talaba:
    def __init__(self, ism, familiya,tyil, password):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.password = password
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
       if fan in self.fanlar:
        self.fanlar.remove(fan)
       else:
            print("Siz bu fanlarga yozilmagansiz")
    def get_info(self):
        fanlar_nomi = [fan.matematika for fan in self.fanlar]
        return f"Talaba: {self.ism}, Fanlar: {fanlar_nomi}"


# TALABA
talaba = Talaba('Alijon', 'Olimov', '2005', 'F1341G5')
# FAN
mathh = Fan('matematika')
fizika = Fan('fizika')
kimyo = Fan('kimyo')
talaba.fanga_yozil(mathh)
print(talaba.get_info())

# O‘CHIRISH
talaba.remove_fan(fizika)

print(talaba.get_info())


class Foydalanuvchi:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def get_info(self):
        return f"{self.ism} {self.familiya}"

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya):
        super().__init__(ism, familiya)

    def ban_user(self, user):
        print(f"{user.ism} bloklandi;")

    def get_info(self):
        return f"Admin: {self.ism} {self.familiya}"

# oddiy user
user1 = Foydalanuvchi("Ali", "Olimov")

# admin
admin = Admin("Hasan", "Karimov")

print(user1.get_info())
print(admin.get_info())

# admin userni bloklaydi
admin.ban_user(user1)