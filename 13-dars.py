#Lugat bilan ishlaymiz


#talaba_0={
#    "ism":"Alijon",
#    "familya":"Shmashiyev",
#    "yosh":24,
#    "fakultet":"Matematika",
#    "kurs":4
#}

#print(talaba_0.items())# items() metodi yordamida lugat ichidagi kalit va qiymatni chiqardik

#for kalit, qiymat in talaba_0.items():
#    print(f"Kalit {kalit}")
#    print(f"Qiyma {qiymat}")




mahuslotlar = {
    "olma":10000,
   "anor":20000,
    "uzum":40000,
    "anjir":25000,

}
print(mahuslotlar.values() )# values() metodi lugatdagi qiymatlarni chiqaradi

telefonlar = {
    "Ali":"iphone x",
    "Vali":"gallayx s9",
    "Hasan":"mi 10 pro",
    "Husan":"iphone x",
    "Orif":"gallayx s9",
    "Nodir":"huawei p30"

}
print("Foydalanuvchilar quyidagi telefonlarni ishlatadilar:")
for tel in telefonlar.values():# values() metodi lugatdagi qiymatlarni chiqaradi
    print(tel.capitalize())
print("Foydalanuvchilar quyidagi telefonlarni ishlatadilar:")
for tel in set(telefonlar.values()):# set() funksiyasi lugatdagi bir necha marotaba qatnashgan malumotlarni faqat bittasini chiqaradi
    print(tel.capitalize())

#print(mahuslotlar.keys())# keys() metodi lugal ichidagi kalit qaytaradi


#print("Dokondagi mahsulotlar:")
#for mahsulot in mahuslotlar:
#    print(mahsulot)


bozorlik = ["olma", "anor", "non", "baliq"]
for mahsulot in mahuslotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.capitalize()} {mahuslotlar[mahsulot]}")


for buyum in bozorlik:
    if buyum not in mahuslotlar:
        print(f"Iltimos dokonizga {buyum} mahsullotni ham olib kelin")