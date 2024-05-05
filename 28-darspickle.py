import pickle

talaba1 = {"ism": "hasan", "familiya": "husanov", "tyil": 2003, "kurs": 2}
talaba2 = {"ism": "alijon", "familiya": "valiyev", "tyil": 2004, "kurs": 1}

with open("info", "wb") as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)




with open("info", "rb") as file:
    talaba1 = pickle.load(file)# loadmetodi file ichini oqiydi
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)