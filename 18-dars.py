def toliq_ism_yasa(ism, familya):
    """Toliq ism familya qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familya}"
    return toliq_ism

talaba = toliq_ism_yasa("olim", "hakimov")
talaba2 = toliq_ism_yasa("hasan", "husanov")
print(f"Darsga kelmagan talabalar: {talaba.title()}, {talaba2.title()}")
print(f"{talaba.title()} darsga kech qolib keldi")
print(f"{talaba2.title()} darsga kelmadi")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {
        "kompaniya": kompaniya,
        "model": model,
        "rang": rangi,
        "korobka": korobka,
        "yil": yili,
        "narh": narhi,
    }
    return avto
avto1 = avto_info('GM', 'gentra', 'qora', 'avtomat', 2024)
avto2 = avto_info('GM', 'malibu', 'oq', 'avtomat', 2024)
avtolar =[avto1, avto2]
print("onlyn bozordagi mavjud moshinalar")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Nomalum"


        print(f"{avto['rang']} {avto['model']}. Narh: {'narh'}")


    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""

    avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting", end="")
        kompaniya = input("\nIshlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input("Korobka: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narh = input("Narhi: ")
        # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
        # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narh))
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob == "no":
            break

print("\nSalonimizdagi avtolar")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = 'nomalum'

    print(f"{avto['rang'].title()} {avto['model'].title()}, {'korobka'} karobka, Narh: {'narh'}")