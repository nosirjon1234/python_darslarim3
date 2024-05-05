#import avto_info_mod #bunda fayillarni chaqiramiz
import avto_info_mod as aim # Bunda fayilni chaqirib unga nom beriladi
#from avto_info_mod import avto_info, info_print #Bunda esa chaqiramiz kegin ichidagi narsalardan foydalanganda funksiya nomini yozmasak boladi



# import avto_info_mod as aim

# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_print(avto1)



# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)

# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)

# from avto_info_mod import *

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)

# avtolar = avtoil.avto_kirit()

# for avto in avtolar:
#     avtoil.info_print(avto)



import math

x=400
print(math.sqrt(x))
print(math.pow(5,2))#pow sonning darajasi


import random as r


son = r.randint(0,10)
javob =("men oylagan sonni yozin")
javob += (f"men oylagan sor oraligi 0dan 10gacha>>>")

ishora = True
while ishora:
    qiymat = input(javob)
    if qiymat == son:
        ishora = False
    if qiymat == 'exit':
        ishora = False
    elif javob == son:
        print("Siz togri topdingiz")
    else:
        print("siz hato topdingiz")

ismlar = ["anvar", "ali", "vali"]
ism = r.choice(ismlar) #lugatdagibironta qiymatni olib beradi
print(ism)

x = list(range(11))
print(x)
r.shuffle(x)# shuffle finksiyasi malumotlarni chalkash qilib tashlaydi
print(x)