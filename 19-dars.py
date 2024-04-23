def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosi kiriting>>>")
        baholar[ism] = int(baho)
    return baholar


talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)

def summa (*sonlar):
    """Kiritligan sonlar yigindisini hisoblaydi"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1,2,3))
print(summa(1,2,3,4,5,6,6))
print(summa(1,2,4,5,6,7,8,9,))


#BUholatda ham ishlasak boladi
def summ (*sonlar):
    """Kiritligan sonlar yigindisini hisoblaydi"""

    return sum(sonlar) #sum degan funksiya jamini hisoblab beradi

print(summa(1,2,3))
print(summa(1,2,3,4,5,6,6))
print(summa(1,2,4,5,6,7,8,9,))