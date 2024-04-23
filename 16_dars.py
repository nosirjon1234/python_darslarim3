#16-dars

print("Yaqin dostalringizni kiriting")

ismlar = []

n=1

while True:
    savol = f"{n}-orindagi dostingizni ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("YAna ism qoshasizmi (ha/yoq) ")
    n+=1
    if takrorlash != 'ha':
         break


print("Dostlaringiz royxati")
for dost in ismlar:
    print(dost.capitalize())


print("Dostlarni tugilgan kunini sawlaymiz")
dostlar = {}
ishora = True
while ishora:
    sim = input("Dostingizni ismini kiriting:")
    yosh = input("Dostingizni tugilgan kun oyini va yilini kiriting: ")
    dostlar[ism] = float(yosh)


    javob = input("yana malumot qoshasizmi? (ha/yoq)")
    if javob == 'yoq':
        ishora = False


for sim,yosh in dostlar.items():
    print(f"{sim.capitalize()}  {yosh} yoshda ")



cars = ["Lasetti", "nexia", "malibu", "tayota", "nexia", "gentra", "nexia"]
while 'nexia' in   cars:
    cars.remove("nexia")

print(cars)


talabalar = ["hasan", "husan", "ali", "vali"]
baholangan_talabalr = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.capitalize()} ning bahosini kiriting")
    print(f"{talaba.capitalize()} baholandi")
    baholangan_talabalr[talaba] = int(baho)

print(baholangan_talabalr)