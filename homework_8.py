oilam = {'akam':'Azizbek'}
oilam['t_yil'] = 2001
oilam['yosh'] = 25
print(f" {oilam['akam'].title()} ,\
 {oilam['t_yil']}-yilda tug'ilgan ,\
 {oilam['yosh']}-yoshda")
print(oilam)

print()

sevimli_taomlar = {
    'otam_taomi':'osh',
    'onam_taomi':'salatlar',
    'akam_taomi':'steak'
  }
print(f"Otam {sevimli_taomlar['otam_taomi'].title()}ni yaxshi ko'radi")
print(f"Onam {sevimli_taomlar['onam_taomi'].title()}ni yaxshi ko'radi")
print(f"Akam {sevimli_taomlar['akam_taomi'].title()}ni yaxshi ko'radi")

izohli_lugat = {
    'lug\'at_1':'for',
    'lug\'at_2':'if',
    'lug\'at_3':'elif',
    'lug\'at_4':'else',
    'lug\'at_5':'input',
    'lug\'at_6':'integer',
    'lug\'at_7':'float',
    'lug\'at_8':'string',
    'lug\'at_9':'f_string',
    'lug\'at_10':'get',

}
print(izohli_lugat)
print()

sorov = input("Quyidagilardan qaysi birini bilmoqchisiz? ")

if sorov == 'for':
    print("For takrorlash operatori, yani har birini birma-bir tekshiradi")
elif sorov == 'if':
    print("If shart berish operatori,yani bir gapni rost yoki yolgon ekanlgini bilish ")
elif sorov == 'elif':
    print("Elif yordamida shartlarni birma bir tekshirish mumkin")
elif sorov == 'input':
    print("Input yordamida biz foydalanuvchidan biron nima so'rashimiz mumkin")
elif sorov == 'integer':
    print("Integer bu butun sonni anglatadi")
elif sorov == 'float':
    print("Float bu o'nlik sonni anglatadi")
elif sorov == 'string':
    print("String bu ma'lumot turi")
elif sorov == 'get':
    print("Get bu sugurib olish va ozgarish kirtish uchun, yani faqat lugat bilan ishalsh mumkin")
else:
    print("Bunday lug'at nomi mavjud emas")
print(sorov)
