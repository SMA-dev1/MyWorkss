# Elektron Pochta Manzillarini Tekshirish:
pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
for email in pochtalar:
    if '@' not in email:
        print("Notogri email:", email)

# parollarni tekshirish
parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
for passwords in parollar:
    if  len(passwords) >= 8:
        print("Juda qisqa:", passwords)
    elif passwords.isalpha():
        print("Kuchsiz parol:", passwords)
    else:
        print("Kuchli parol:", passwords)

 # Ob-havo Ma'lumotlarini Tahlil Qilish
haroratlar = [20, 22, 19, 24, 25, 23, 21]
orta = sum(haroratlar) / len(haroratlar)
print("Ortacha harorat:", orta)
for harorat in haroratlar:
    if harorat > 22:
        print("Ilik kun:", harorat)
    else:
        print("Salqin kun:", harorat)

# restoran buyurtmalari
taomlar = ["Osh", "Shashlik", "Manti", "Lag'mon"]

buyurtma = input("Qaysi taomni buyurtma qilasiz: ")

bor = False

for taom in taomlar:
    if  buyurtma == taom.lower():
        bor = True

if bor:
    print("Buyurtmangiz qabul qilindi")
else:
    print("Kechirasiz, bunday taom yo'q")
