class Avto:
    def __init__(self, model, rang, karobka, narh, chyil):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.chyil = chyil
        self.kilometr = 0
    def get_info(self):
        return f"Mashinaning modeli: {self.model}, Rangi: {self.rang}, Karobkasi: {self.karobka}, Narhi: {self.narh}$, Chiqqan yili: {self.chyil}, Qancha yurgani: {self.kilometr} km "

    def set_kilometr(self, kilometr):
        self.kilometr = kilometr

    def update_kilometr(self):
        self.kilometr += 1

avto1 = Avto('Cobalt', 'Oq', 'Mexanik', '14000', '2022')
print(avto1.get_info())

avto1.kilometr = 20
print(avto1.kilometr)
print(avto1.get_info())

avto1.set_kilometr(30)
print(avto1.get_info())

avto1.update_kilometr()
print(avto1.get_info())

class Avto:
    def __init__(self, model, rang, narx):
        self.model = model
        self.rang = rang
        self.narx = narx

    def get_info(self):
        return f"Model: {self.model}, Rang: {self.rang}, Narx: {self.narx}"


class Avtosalon:
    def __init__(self, salon_nomi, manzil):
        self.salon_nomi = salon_nomi
        self.manzil = manzil
        self.sotuvdagi_mashinalar = []

    def add_avto(self, avto):
        self.sotuvdagi_mashinalar.append(avto)

    def get_avtolar(self):
        return [avto.get_info() for avto in self.sotuvdagi_mashinalar]


# Avtolar yaratamiz
avto1 = Avto("Chevrolet Malibu", "oq", 25000)
avto2 = Avto("Kia K5", "qora", 30000)
avto3 = Avto("BYD Song Plus", "ko‘k", 28000)

# Avtosalon yaratamiz
salon = Avtosalon("GM Uzbekistan", "Toshkent")

# Avtolarni qo‘shamiz
salon.add_avto(avto1)
salon.add_avto(avto2)
salon.add_avto(avto3)

# Natija chiqaramiz
for avto in salon.get_avtolar():
    print(dir(avto))