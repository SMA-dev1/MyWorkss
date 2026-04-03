davlatlar = ["Makkah", "Shvetsariya", "Italiya", "Meksika"]
print("sorted() ro'yhat: ", sorted(davlatlar) )
print("Asl ro'yhat: ", davlatlar)

# tartiblangan holda sort()
davlatlar = ["Makkah", "Shvetsariya", "Italiya", "Meksika"]
davlatlar.sort()
print(davlatlar)

# teskari tartib sort(reverse=True)
davlatlar = ["Makkah", "Shvetsariya", "Italiya", "Meksika"]
davlatlar.sort(reverse=True)
print(davlatlar)

# ortidan oldinga yani reverse()
davlatlar = ["Makkah", "Shvetsariya", "Italiya", "Meksika"]
davlatlar.reverse()
print(davlatlar)

# 120 dan 1200 gacha royhat
print(list(range(120,1200,2)))

# hisoblash
sonlar = [12, 145, 3254, 326, 436]
arzon = min(sonlar)
qimmat = max(sonlar)
jami = sum(sonlar)
print("Eng arzoni: ",arzon, " Eng qimmati: ",qimmat, " Jami: ",jami)

# nusxa olish
taomlar = ["xurmo", "o'rik", "gilos", "olxo'ri"]
nonushta = taomlar[:]
nonushta.append("uzum")
nonushta.append("olcha")
print("taomlar ro'yhati: ", taomlar)
print("Nonushtaga yeyiladigan taomlar: " ,nonushta)

nonushta0 = ("qaymoq","non")
print(nonushta0)
