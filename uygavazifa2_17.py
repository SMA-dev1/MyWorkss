file = open("pi_million_digits.txt", "r")
pi_matn = file.read()
file.close()

tugilgan_sana = input("Tug‘ilgan sanani kiriting (DDMMYYYY): ")

if tugilgan_sana in pi_matn:
    print("Bor ekan!")
else:
    print("Yo‘q ekan!")
# matn listga otkazish
import pickle
# pi matn listga otkazish
def save_pi_as_list(pi_digits, filename):
    pi_list = list(pi_digits)

    with open(filename, 'wb') as file:
        pickle.dump(pi_list, file)

    print("Ma'lumot pickle orqali saqlandi.")
save_pi_as_list(pi_matn, "pi_data.pkl")

# Faylga saqlash
def user_data_append(filename):
    print("Ma'lumot kiriting (to‘xtatish uchun 'exit'):")

    while True:
        data = input("> ")
        if data.lower() == 'exit':
            break

        with open(filename, 'a') as file:
            file.write(data + '\n')

    print("Ma'lumotlar saqlandi ✅")