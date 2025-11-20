import math

class Tvar:
    def obsah(self):
        print("není definováno")
        


class Ctverec(Tvar):
    def __init__(self, hrana):
        self.hrana = hrana
    
    def obsah(self):
        return self.hrana * self.hrana


class Kruh(Tvar):
    def __init__(self, polomer):
        self.polomer = polomer

    def obsah(self):
        return math.pi * self.polomer * self. polomer



if __name__ == "__main__":

    tvary = [Ctverec(2), Ctverec(3), Kruh(2), Ctverec(1), Kruh(1)]

    suma = 0
    for tvar in tvary:
        suma += (tvar.obsah())
    print(f"Suma všech tvarů je: {suma}")

    #obj1 = Ctverec(6)
    #print(obj1.obsah())
    #obj2 = Kruh(3)
    #print(obj2.obsah())