#input va while





s = "Ismingizni kiriting!"
s +=f"(dasturni toxtatish uchun 'exit' deb yozin):"
ishora = True
while  ishora:
    qiymat = input(s)
    if qiymat == 'exit':
        ishora = False
    elif qiymat == "Nosirjon":
        print("Assalomu alykum admin")
        break# break tsikilni toxtatadi
    else:
        print("Assalomu alaykum siz admin emassiz")
        break
print("dastur toxtatildi")



print("Kiritilgan sonning kivadratini qaytaruvchi dastur")
s = "Istagan soningizni kiritn!"
s +=f"(dasturni toxtatish uchun 'exit' deb yozin):"
ishora = True
while  ishora:
    qiymat = input(s)
    if qiymat == 'exit':
        ishora = False

    else:
        print(float(qiymat)**2)
print("dastur toxtatildi")



sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue# son 5ga kelganda continue kodni oqimasdan tepaga chiqar vordi
    print(f"{son} sonining kvadrati {son**2} ga teng")

raqam = 0
while raqam<10:
    raqam+=1
    if raqam%2 != 0:# bu shartda sonni juftlarini consolga chiqaryapmiz
        continue
    else:print(raqam)
