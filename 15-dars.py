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



