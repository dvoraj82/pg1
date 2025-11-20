class BankovniUcet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0

    def vloz(self, suma):
        self.suma = suma
        if suma >= 0:
            self.__zustatek += suma
            print(f"Vložili jste {suma} a nový zůstatek je {self.__zustatek}")
        else:
            print("Částka pro vklad musí být kladná.")

    def vyber(self, suma):
        self.suma = suma
        if 0 < suma <= self.__zustatek:
            self.__zustatek -= suma
            print(f"Vybrali jste {suma} a nový zůstatek je {self.__zustatek}")
        else:
            print("Nedostatečný zůstatek nebo neplatná částka pro výběr.")

    def __str___(self):
        print(f"Účet vlastí {self.majitel} a je na něm {self.__zustatek}")


if __name__ == "__main__":
    ucet = BankovniUcet("Alice")
    print(ucet)

    ucet.vloz(100)
    print(ucet)

    ucet.vyber(50)
    print(ucet)

    ucet.vloz(-10)
    print(ucet)

    ucet.vyber(1000)
    print(ucet)
