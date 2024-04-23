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