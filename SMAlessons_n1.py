# capitalize()	Converts the first character to upper case
Ism = "anvarbek"
ism = Ism.capitalize()
print(ism)

txt = "hello world"
x = txt.capitalize()
print(x)

# casefold()	Converts string into lower case
telefon = "telefon"
phono = telefon.casefold()
print(phono)

nik = "salom ali"
cefr = nik.casefold()
print(cefr)

# center()	Returns a centered string
text = "benji"
x = text.center(12)
print(x)

sumka = "shirina"
romolcha = sumka.center(23)
print(romolcha)

# count()	Returns the number of times a specified value occurs in a string
fish = "maybash"
qarmoq = fish.count("m")
print(qarmoq)

kubik = "sariq"
rubik = kubik.count("r")
print(rubik)

# encode()	Returns an encoded version of the string
monitor = "oyna"
qora = monitor.encode()
print(qora)

notbuk = "qizil"
yashik = notbuk.encode()
print(yashik)

# endswith()	Returns true if the string ends with the specified value
malibu2 = "qorasidan"
malibu3 = malibu2.endswith("o")
print(malibu3)

cobalt = "555"
chev = cobalt.endswith(".")
print(chev)

# expandtabs()	Sets the tab size of the string
gold = "karnay"
maker = gold.expandtabs(2)
print(maker)

mishka = "led"
usb = mishka.expandtabs(2)
print(usb)

# find()	Searches the string for a specified value and returns the position of where it was found
shelf = "kurtka"
suit = shelf.find("k")
print(suit)

gilam = "door"
window = gilam.find("j")
print(window)

# format()	Formats specified values in a string
parta = "grown"
gray = parta.format()
print(gray)

zashitnik = "yashil"
green = zashitnik.format()
print(green)

# format_map()	Formats specified values in a string
quloqchin = "Bu {narsa}"
data = {"narsa": "noushnik"}
kokidan = quloqchin.format_map(data)
print(kokidan)

tv = "Bu {narsa}"
data = {"narsa": "tv"}
ekran = quloqchin.format_map(data)
print(ekran)

# index()	Searches the string for a specified value and returns the position of where it was found
yangilik = "salom, hammaga"
zamon = yangilik.index("hammaga")
print(zamon)

aipods = "qorasi,udari"
airpods = aipods.index("udari")
print(aipods)

# isalnum()	Returns True if all characters in the string are alphanumeric
yuk = "company12"
uk = yuk.isalnum()
print(uk)

moshin = "ogir"
yukmashin = moshin.isalnum()
print(yukmashin)

# isalpha()	Returns True if all characters in the string are in the alphabet
jok = "100$"
choqchoq = jok.isalnum()
print(choqchoq)

ordak = "oq"
kaptar = ordak.isalnum()
print(kaptar)

# isascii()	Returns True if all characters in the string are ascii characters
huk = "lik"
kil = huk.isascii()
print(kil)

full = "kema"
wip = full.isascii()
print(wip)

# isdecimal()	Returns True if all characters in the string are decimals
fel = "leader"
led = fel.isdecimal()
print(led)

battery = "kok"
loki = battery.isdecimal()
print(loki)

# isdigit()	Returns True if all characters in the string are digits
opit = "pito"
pilof = opit.isdigit()
print(pilof)

get = "get tore"
wer = get.isdigit()
print(wer)


# isidentifier()	Returns True if the string is an identifier
sed = "123"
der = sed.isidentifier()
print(der)

asmaster = "toj"
qzi = asmaster.isidentifier()
print(qzi)


# islower()	Returns True if all characters in the string are lower case
tel = "contact"
t95 = tel.islower()
print(t95)

kul = "qwe"
was = kul.islower()
print(was)


# isnumeric()	Returns True if all characters in the string are numeric
joke = "."
lol = joke.isnumeric()
print(lol)

u87 = "liop"
hup = u87.isnumeric()
print(hup)

# isprintable()	Returns True if all characters in the string are printable
vip = "gol"
hog = vip.isprintable()
print(hog)

qwerty = "12345"
ul = qwerty.isprintable()
print(ul)

# isspace()	Returns True if all characters in the string are whitespaces
qas = "saq"
dog = qas.isspace()
print(dog)

july = "like"
sofar = july.isspace()
print(sofar)

# istitle()	Returns True if the string follows the rules of a title
bet = "betwars"
wde = bet.istitle()
print(wde)

der = "www"
wwe = der.istitle()
print(wwe)

# isupper()	Returns True if all characters in the string are upper case
nitro = "use"
until = nitro.isupper()
print(until)

web = "site"
best = web.isupper()
print(best)

# join()	Joins the elements of an iterable to the end of the string
w21 = ("78jo","tul","kult")
jo78 ="#".join(w21)
print(jo78)

rer = ("fot", "gt","fr")
rep = "#".join(rer)
print(rep)

# ljust()	Returns a left justified version of the string
ert = "dert"
ft = ert.ljust(4)
print(ft)

qws = "qwz"
ssd = qws.ljust(3)
print(ssd)

# lower()	Converts a string into lower case
use = "zs"
cf = use.lower()
print(cf)

yut = "ichinga"
please = yut.lower()
print(please)


# lstrip()	Returns a left trim version of the string
hut = "gut"
sarvin = hut.lstrip()
print(sarvin)

cerf = "sefr"
fery = cerf.lstrip()
print(fery)


# maketrans()	Returns a translation table to be used in translations
tut = "pol"
lot = tut.maketrans("P","l")
print(lot)

kuoly = "ctg"
jul = kuoly.maketrans("c","g")
print(jul)

# partition()	Returns a tuple where the string is parted into three parts
vop = "jota ate apple"
got = vop.partition("apple")
print(got)

trt = "suiii"
tes = trt.partition("i")
print(set)


# replace()	Returns a string where a specified value is replaced with a specified value
y56 = "h89"
nit = y56.replace("banana","apple")
print(nit)

cuut = "good"
ert = cuut.replace("good","banana")
print(ert)

# rfind()	Searches the string for a specified value and returns the last position of where it was found
turit = "mi turist, su turist"
serit = turit.rfind("turist")
print(serit)

sew = "golly"
ketty = sew.rfind("golly")
print(ketty)


# rindex()	Searches the string for a specified value and returns the last position of where it was found
tur = "it"
toh = tur.rindex("it")
print(toh)

cale = "joti"
volli = cale.rindex("joti")
print(volli)

# rjust()	Returns a right justified version of the string
mop = "buti"
nuti = mop.rjust(12)
print(nuti)

teri = "oqqi"
oqidan = teri.rjust(9)
print(oqidan)


# rpartition()	Returns a tuple where the string is parted into three parts
verty = "perefer"
xeryt = verty.rpartition("perefer")
print(xeryt)

goldy = "bocksi"
zar = goldy.rpartition("bocksi")
print(zar)

# rsplit()	Splits the string at the specified separator, and returns a list
nopm = "vcm"
rkm = nopm.rsplit("vcm")
print(rkm)


ilm = "dargoh"
cfs = ilm.rsplit("dargoh")
print(cfs)

# rstrip()	Returns a right trim version of the string
cnm = "gop"
zum = cnm.rstrip("gop")
print(zum)

boyka = "4qism"
urw = boyka.rstrip("4qism")
print(urw)


# split()	Splits the string at the specified separator, and returns a list
bon = "jolly"
zx = bon.split("jolly")
print(zx)

nonnie = "ronnie"
nope = nonnie.split("ronnie")
print(nope)

# splitlines()	Splits the string at line breaks and returns a list
ji = "mi"
lok = ji.splitlines()
print(lok)

xmz = "zxm"
mn = xmz.split("zxm")
print(mn)

# startswith()	Returns true if the string starts with the specified value
nollp =" bolt"
vicm = nollp.startswith("bolt")
print(vicm)

holly = "wkl"
walk = holly.startswith("wkl")
print(walk)


# strip()	Returns a trimmed version of the string
polly = "k90"
p90 = polly.strip("k90")
print(p90)

wwe = "2k"
kda2 = wwe.strip("2k")
print(kda2)


# swapcase()	Swaps cases, lower case becomes upper case and vice versa
p91 = "4 quril"
jok = p91.swapcase()
print(jok)

gert = "ukol"
m5lg = gert.swapcase()
print(m5lg)


# title()	Converts the first character of each word to upper case
qolli = "[]"
nit = qolli.title()
print(nit)

killo = "polov"
necha = killo.title()
print(necha)

# translate()	Returns a translated string
molka = "shuka"
moda = molka.translate(str.maketrans('',''))
print(moda)

dmyomon = "yomonmas"
yoqay = dmyomon.translate(str.maketrans('',''))
print(yoqay)



# upper()	Converts a string into upper case
billiard = "9ball"
pollday = billiard.upper()
print(pollday)

desert = "deust2"
dedust = desert.upper()
print(dedust)


# zfill()	Fills the string with a specified number of 0 values at the beginning
ops = "shock"
meme = ops.zfill(4)
print(meme)

sopt = "posting"
zort = sopt.zfill(3)
print(zort)
