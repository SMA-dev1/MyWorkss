# # Quyidagi ma’lumotdan har bir o‘quvchining o‘rtacha bahosini hisoblang.
#
# students = {
#     "Ali": [80, 90, 85],
#     "Vali": [70, 60, 75],
#     "Sami": [95, 88, 92]
# }
# for ism, baholar in students.items():
#     yigindi = 0
#
#     for baho in baholar:
#         yigindi = yigindi + baho
#
#     ortacha = yigindi / len(baholar)
#
#     print(ism, "ortachasi", ortacha)

# Narxi 100 dan katta bo‘lgan mahsulotlarni chiqaring.

# products = [
#     {"name":"olma", "price":120},
#     {"name":"anor", "price":90},
#     {"name":"banan", "price":150}
# ]
# for product in products:
#     if product["price"] > 100:
#      print(product["name"],"-", product["price"])
# 18 yoshdan katta foydalanuvchilarni chiqaring.

# users = [
#     {"name":"Ali", "age":20},
#     {"name":"Vali", "age":16},
#     {"name":"Sami", "age":25}
# ]
#
# for user in users:
#     if user["age"] > 18:
#         print(f"{user['name']} ovoz berishi mumkin ")
#     else:
#         print(f"{user['name']} siz 18 yoshdan kichiksiz ")
# # Har bir kursdagi o‘quvchilar sonini aniqlang.
#
# courses = {
#     "python": ["Ali","Vali","Sami"],
#     "django": ["Ali","Sami"],
#     "ai": ["Vali","Sami","Jasur"]
# }
# for course in courses:
#     soni = len(courses[course])
#     print(f"{course}: {soni}")
#

# # Eng katta sonni toping:

# numbers = [
#     [4,7,2],
#     [9,1,5],
#     [3,8,6]
# ]
# max_number = numbers[0][0]
#
# for qator in numbers:
#     for number in qator:
#         if number > max_number:
#             max_number = number
# print(max_number)

# # Faqat active foydalanuvchilarni chiqaring.
#
# data = {
#     "users":[
#         {"name":"Ali", "active":True},
#         {"name":"Vali", "active":False},
#         {"name":"Sami", "active":True}
#     ]
# }
#
# for user in data["users"]:
#     if user["active"]:
#         print(f"{user['name']} is {user['active']}")
