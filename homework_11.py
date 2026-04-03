# togri_ranglar = ("sariq", 'qizil', 'yashil')
# while True:
#     rang = input(" Rang kiriting: ")
#
#     if rang in togri_ranglar:
#         print("rahmat, to‘g‘ri keladi")
#         break
# else:
#       print("rang kiriting")

# import random
#
# tasodifiy_son = random.randint(1, 10)
#
# while True:
#     sonlar = int(input("1 dan 10 gacha son oylab yozing: "))
#     if sonlar == 8:
#      if sonlar != tasodifiy_son:
#         print("Tabriklaymiz! siz topdingiz. ")
#         break
#      else:
#         print("Notogri! qaytadan urunib koring:")
#
#
# ismlar = []
#
# print("Do'stlarni ro'yhatini tuzamiz:")
# n=1
# ish = True
# while ish:
#     savol = f"{n} do'stingizni ismini kiriitng:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi: (yes/no):")
#     if javob == "yes":
#         continue
#         n+=1
#     else:
#         break
#
# print("Do'stlaringizni ro'yhati")
# for ismini in ismlar:
#     print(ismini)

# print("Bu yerda valyuta kursini bilib oling>>>")
# kurs = 12600  # 1 USD = 12600 so'm
#
# while True:
#     qiymat = input("Summani kiriting (yoki 'exit'): ")
#
#     if qiymat == "exit":
#         print("Siz bilan ishlash maroqli bo'ldi!")
#         break
#     # try va except yangi qo'llanma
#     try:
#         summa = float(qiymat)
#         dollar = summa / kurs
#         print(f"{dollar} dollar")
#     except:
#         print("Iltimos, faqat son kiriting!")
#
