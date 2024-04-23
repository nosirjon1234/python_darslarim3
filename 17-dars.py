#funksiya bilan ishlash

def salom_ber(ism, yosh): #def bu biz hozir funksiya yaritishimizni anglatadi
    """Foydalanuvchidan ismini qabul qilib,
        unga salom beruvchi funksiya"""

    print(f"Assalomu alaykum, hurmatli {ism.capitalize()} siz {yosh} yoshdasiz")

salom_ber("olim", 15)

def toliq_ism(ism, familya):
    """Foydalanuvchidan ismini va familyasini qabul qilib
        unga salom beruvchi funksiya"""
    print(f"Foydalanuvchining ismi: {ism.capitalize()}\n"
          f"Foydalanuvchining familyasi: {familya.capitalize()}")

toliq_ism("nosirjon", "yoldashev")

def toliq_ism(ism, tugilgan_yili):
    """Foydalanuvchidan ismini va familyasini qabul qilib
        unga salom beruvchi funksiya"""
    print(f"Foydalanuvchining ismi: {ism.capitalize()}\n"
          f"Foydalanuvchining yoshi: {2024-tugilgan_yili}")

toliq_ism("nosirjon", 2009)
def toliq_ism(ism, familya):
    """Foydalanuvchidan ismini va familyasini qabul qilib
        unga salom beruvchi funksiya"""
    print(f"Foydalanuvchining ismi: {ism.capitalize()}\n"
          f"Foydalanuvchining familyasi: {familya.capitalize()}")

toliq_ism(ism="nosirjon", familya="yoldashev")#bu holatda ham funksiya chaqirsak boladi

def yosh_hisobla(tugilgan_yil, joriy_yil = 2024):
    """Foydalanuvchini tugilgan yilga qarab yoshini chiqarib beruvchi funksiya"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

print(2009, 2024)#bu haltda ham yozsak boladi
print(2009)#bu holatda ham yozsak boladi chunki tepada joriy_yilga qiymat berib qoyganmiz