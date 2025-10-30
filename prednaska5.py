class Chybadeleninulou(Exception):
    pass

def vydel(citatel, jmenovatel):
    if jmenovatel == 0:
        raise Chybadeleninulou("Nulou nelze dělit")
    return citatel / jmenovatel

if __name__ == "__main__":
    
    try:

        cislo1 = None
        while cislo1 is None:
            try:
                cislo1 = int(input("Zadej čitatel: "))
            except Exception:
                print("Zadej správně číslo!")
    
        cislo2 = int(input("Zadej jmenovatel: "))

        vysledek = vydel(cislo1, cislo2)

        print(vysledek)

    except Chybadeleninulou as e:
        print("Pokusili jste se dělit nulou!!")

    except Exception as e:

        print(f"V našem programu nastala chyba: {e}")
    