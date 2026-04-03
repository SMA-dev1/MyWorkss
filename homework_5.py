foydalanuvchilar = input(" Yangi login kiritng: \n >>> ")
if foydalanuvchilar != "anvar":
    print("Xush kelibsiz!")
else:
    print("Bu login band, iltimos boshqa login kiriting")

son = int(input(" Juft son kiriting: \n >>> "))
if son % 2 == 0:
    print("Raxmat!")
else:
    print("Bu son juft emas!")

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

if son1 > son2:
    print(son1, ">", son2)
else:
    print(son1, "<", son2)