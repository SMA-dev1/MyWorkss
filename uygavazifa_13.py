def kopaytma(*sonlar):
    """Istalgan sonni kopaytmasi"""
    natija = 1 # yoki istalgan sonni yozing
    for son in sonlar:
        natija *= son
    return natija
print(kopaytma(2,3,4))


# talaba information
def talaba_info(ism,familiya,**malumotlar):
    talaba = {
        'familiya':familiya,
        'ism':ism
    }
    return talaba
print(talaba_info('Alibek','Alijanov',kurs=2, yosh=24))

# Chegirma hisoblash

def total_price(*narxlar, **kwargs):
    jami = sum(narxlar)
    discount = kwargs.get("discount", 0)

    if discount:
        jami -= jami * discount / 100

    return jami
print(total_price(10000, 20000, 15000, discount=10))

#matnlarni ajratish:

def join_words(*sozlar, **kwargs):
    sep = kwargs.get("sep", " ")
    return sep.join(sozlar)

print(join_words("Python", "is", "awesome", sep="-"))