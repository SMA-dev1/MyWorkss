# izohli_lugat = {
#     'Boolean':'Mantiqiy son',
#     'Integer':'Butun son',
#     'Float':'onlik son',
#     'String':'matn',
#     'For':'takrorlsh',
#     'List':'ro\'yhat',
#     'Tuple':'ozgarmas ro\'yhat',
#     'Dict':'lug\'at',
# }
# for key,value in sorted(izohli_lugat.items()):
#  print(f"{key} - {value}")
#  #
countries = {
    'aqsh':'Washington D.C.',
    'italiya':'Rim',
    'malayziya':'Kuala-Lumpur',
    'o\'zbekiston':'Toshkent',
    'qirg\'iziston':'Bishkek',
    'qozog\'iston':'Nursulton',
    'rossiya':'Moskva',
    'singapur':'Sungapur',
    'tojikiston':'Dushanbe',
 }
print("Davlatlarning nomlari ")
for country in sorted(countries.keys()):
    print(f"{country.title()}")

print("Davlatlarning poytaxtlari: ")
for poytaxt in sorted(countries.values()):
    print(f"{poytaxt.title()}")


davlat = input("Qaysi davlatni poytaxtini bilmoqchisiz: ")
if davlat in countries:
    print(f"{davlat.title()} ning poytaxti {poytaxt.title()}")
else:
    print("Bizda bunday ma\'lumot yo\'q")

menu = {
    'osh':45000,
    'somsa':12000,
    'shashlik':9000,
    'gamburg':18000,
    'lavash':35000,
    'lag\'mon':25000,
    'o\'rama patir':28000,
    'gumma':7000,
    'qovurilgan baliq':68000,
    'grill tovuq':70000,
    'steak':99000,
}
print("3 ta taom nomini kirting: ")
buyurtma = []
for x in range(3):
    taom = input(f"{x+1}-taom: ").lower()
    buyurtma.append(taom)
for buyurtmalar in buyurtma:
    if buyurtmalar in menu:
     print(f"{buyurtmalar.title()} {menu[buyurtmalar]} so'm")
    else:
        print("Bizda bunday taom yo\'q")
