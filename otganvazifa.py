# 1 - topshiriq
def foydalanuvchi(ism, familiya, yil, joy, email=None, tel=None):
    yosh = 2026 - yil  # oddiy hisob

    user = {
        "ism": ism,
        "familiya": familiya,
        "tugilgan_yil": yil,
        "tugilgan_joy": joy,
        "yosh": yosh
    }

    if email:
        user["email"] = email
    if tel:
        user["telefon"] = tel

    return user

# Misol
print(foydalanuvchi("Ali", "Valiyev", 2005, "Toshkent"))

print("-----------------------------------")

# 2
mijozlar = []

i = 0
while i < 2:  # 2 ta misol uchun
    ism = input("Ism kiriting: ")
    familiya = input("Familiya kiriting: ")
    yil = int(input("Tug'ilgan yil: "))
    joy = input("Tug'ilgan joy: ")

    user = foydalanuvchi(ism, familiya, yil, joy)
    mijozlar.append(user)

    i += 1

print(mijozlar)

print("-------------------")

# 3
def eng_katta(a, b, c):
    return max(a, b, c)

print(eng_katta(10, 25, 7))

print("-=-=-=-=-=-=-==-=--=-")

# 4
import math

def aylana(radius):
    diametr = 2 * radius
    perimetr = 2 * math.pi * radius
    yuza = math.pi * radius ** 2

    return {
        "radius": radius,
        "diametr": diametr,
        "perimetr": perimetr,
        "yuza": yuza
    }
print(aylana(5))
print("------++++-------")

# 5
def tub_sonlar(n):
    natija = []

    for son in range(2, n+1):
        tub = True
        for i in range(2, son):
            if son % i == 0:
                tub = False
                break
        if tub:
            natija.append(son)

    return natija

# Misol ishlimiz
print(tub_sonlar(20))

print('***********************')
# 6
def fibonacci(n):
    sonlar = [1, 1]

    while len(sonlar) < n:
        yangi = sonlar[-1] + sonlar[-2]
        sonlar.append(yangi)

    return sonlar

# Misol
print(fibonacci(10))