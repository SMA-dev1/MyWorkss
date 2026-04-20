import datetime as dt
# # Necha kun qolgani korish
# bugun = dt.date.today()
# ramozon_qurbon_hayit = dt.date(2026, 5 , 27)
# farq = ramozon_qurbon_hayit-bugun
# print(farq)
# print(f" Ramozon hayitga {farq.days} kun qoldi")

# 10 ta sana kiritish
# from datetime import datetime, timedelta
#
# bugun = datetime.today()
#
# for f in range(10):
#     yangi_sana = bugun + timedelta(days=14 * f)
#     print(yangi_sana.strftime("%d/%m/%Y"))
#
# # 3 topahiriq
# from datetime import datetime
#
# # Tug‘ilgan kundan hozirgacha qancha vaqt o‘tgan
# tugilgan = input("Tug‘ilgan kunigizni sanasini kiriting(YYYY-MM-DD): ")
# tugilgan = datetime.strptime(tugilgan, "%Y-%m-%d")
#
# bugun = datetime.today()
#
# farq = bugun - tugilgan
#
# yil = farq.days // 365
# oy = (farq.days % 365) // 30
# kun = (farq.days % 365) % 30
#
# print(yil, "yil", oy, "oy", kun, "kun")
# print(f"Kun {farq.days} otgan")

# Foydalanuvchini tel raqami togri yoki notogriliki
import re
#
# telefon_nomer = input('Iltimos telefon raqamingizni kiriting: ')
#
# andoza =  r'^\+998\d{9}$'
# if re.fullmatch(andoza, telefon_nomer):
#     print('Telefon raqamingiz togri kiritildi: ')
# else:
#     print('Telefon raqamingiz notogri kiritildi: ')
#
# print(re.match(andoza, telefon_nomer))


matn = """Assalomu alaykum hurmatli obanet qanday savollaringizni bolsa shu pochtaga yani anvar@gmail.com ga yuboring"""

andozaa = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

email = re.findall(andozaa, matn)
print(email)