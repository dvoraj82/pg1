import sys

# napište funkci spocitej_statistiku(text), která přijme jeden parametr:
# text – řetězec obsahující více řádků textu
# Funkce vrátí tři hodnoty:
# počet řádků v textu
# počet slov v textu (slovo je sekvence znaků oddělená mezerami nebo koncem řádku)
# počet znaků v textu (včetně mezer a konců řádků)

def spocitej_statistiku(text):

    pocet_radku = 0
    pocet_slov = 0
    pocet_znaku = 0

    #První možný řešení
    #pocet_radku = len(text.split('\n'))
    #pocet_slov = len(text.split())
    #pocet_znaku = len(text)

    #Druhý možný řešení (je efektivnější, protože se text projde jen jednou)
    for x in text:
        pocet_znaku += 1
        if x == '\n':
            pocet_radku += 1
            pocet_slov += 1
        if x == " ":
            pocet_slov += 1
    
    if pocet_znaku > 0:
        pocet_radku += 1


    # Vaše řešení zde

    return pocet_radku, pocet_slov, pocet_znaku


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pouziti: python program.py vstupni_soubor")
        sys.exit(1)
    vstupni_soubor = sys.argv[1]

    try:
        with open(vstupni_soubor, "r", encoding="utf-8") as f:
            obsah = f.read()

        pocet_radku, pocet_slov, pocet_znaku = spocitej_statistiku(obsah)

        print(f"Pocet radku: {pocet_radku}")
        print(f"Pocet slov: {pocet_slov}")
        print(f"Pocet znaku: {pocet_znaku}")


    #výjimka se vyvolává pomocí raise
    except FileNotFoundError:
        print("Vstupni soubor neexistuje")
    except Exception:
        print("Doslo k chybe pri praci se souborem")