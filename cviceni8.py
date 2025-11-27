import sys
import json

class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, prijmeni, tel, vek, email):
        self.__jmeno = jmeno
        self.prijmeni = prijmeni
        self.tel = tel
        self.vek = vek
        self.email = email
    
    @property
    def jmeno(self):
        return self.__jmeno
    
    @jmeno.setter
    def jmeno(self, hodnota:str):
        for c in hodnota:
            if not (c.isalpha() and not c.isspace()):
                raise InvalidData(f"Chybe zadane jmeno: {hodnota}")
        self.__jmeno = hodnota

    @property
    def tel(self):
        return self.__tel
    
    @tel.setter
    def tel(self, hodnota:str):
        if not len(hodnota) == 13:
            raise InvalidData("Číslo musí mít 13 znaků")
        if hodnota[0] != "+":
            raise InvalidData("Číslo musí začínat znakem +")
        if hodnota[1:].isdigit():
            raise InvalidData("Není číslo")
        self.__tel = hodnota

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, hodnota:str):
        if "@" not in hodnota:
            raise InvalidData("Chybný email, chybí @")
        if not hodnota.endswith(".cz"):
            raise InvalidData("Chybný email, musí končit na .cz")
        if not hodnota.replace("@", "").replace(".", "").isalnum():
            raise InvalidData("Email obsahuje nepovolené znaky")
        self.__email = hodnota

    def __str__(self):
        return f"Osoba: {self.jmeno} {self.prijmeni}, tel: {self.tel}, vek: {self.vek}"
    

if __name__ == "__main__":

    o1 = Osoba("Jan", "Novak", "+420123456789", 30, "novak@seznam.cz")
    print(o1)

    o1.jmeno = "Tomáš"
    print(o1)