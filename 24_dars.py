# klasslar


class Talaba:
    def __init__(self, ism, familya, yosh): # __init__ talaba kilasidan obyek yaratadi
        self.ism = ism
        self.familya = familya
        self.yosh = yosh
    def get_name(self):
        return self.ism
    def tanishtir(self):
        return  f"Ismim {self.ism} familyam {self.familya} yoshim {self.yosh} da"



talaba1 = Talaba('Olim', 'Olimov', 22)
talaba2 = Talaba('Izzatillo', 'Alimov', 22)

talaba1.tanishtir()
talaba2.tanishtir()