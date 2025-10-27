def je_tah_mozny_pesec(pozice, cil, obsazene):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cil
    delka_radek, delka_sloupec = cil_radek - radek, cil_sloupec - sloupec

    if delka_sloupec != 0:
        return False
    
    if delka_radek == 1 and (cil_radek, cil_sloupec) not in obsazene:
        return True
    
    if radek == 2 and delka_radek == 2 and (radek + 1, sloupec) not in obsazene and (cil_radek, cil_sloupec) not in obsazene:
        return True
    
    return False
    

def je_tah_mozny_vez(pozice, cil, obsazene):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cil
    delka_radek, delka_sloupec = cil_radek - radek, cil_sloupec - sloupec

    if delka_radek != 0 and delka_sloupec != 0:
        return False
    
    if delka_radek == 0:
        if delka_sloupec > 0:
            krok = 1
        else:
            krok = -1
        for i in range(sloupec + krok, cil_sloupec, krok):
            if (radek, i) in obsazene:
                return False
    else:
        if delka_radek > 0:
            krok = 1
        else:
            krok = -1
        for i in range(radek + krok, cil_radek, krok):
            if (i, sloupec) in obsazene:
                return False
            
    return True


def je_tah_mozny_strelec(pozice, cil, obsazene):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cil
    delka_radek, delka_sloupec = cil_radek - radek, cil_sloupec - sloupec

    if abs(delka_radek) != abs(delka_sloupec):
        return False
    
    if delka_radek > 0:
        krok_radek = 1
    else:
        krok_radek = -1

    if delka_sloupec > 0:
        krok_sloupec = 1
    else:
        krok_sloupec = -1

    for i in range(1, abs(delka_radek)):
        if (radek + i * krok_radek, sloupec + i * krok_sloupec) in obsazene:
            return False
    
    return True


def je_tah_mozny_jezdec(pozice, cil, obsazene):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cil
    delka_radek, delka_sloupec = abs(cil_radek - radek), abs(cil_sloupec - sloupec)
    
    return(delka_radek, delka_sloupec) in [(2, 1), (1, 2)]


def je_tah_mozny_kral(pozice, cil, obsazene):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cil
    
    return abs(cil_radek - radek) <= 1 and abs(cil_sloupec - sloupec) <= 1


def je_tah_mozny_dama(pozice, cil, obsazene):
    
    if je_tah_mozny_vez(pozice, cil, obsazene) or je_tah_mozny_strelec(pozice, cil, obsazene):
        return True
    
    return False





def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.

    typ = figurka["typ"]
    pozice = figurka["pozice"]
    cil_radek, cil_sloupec = cilova_pozice


    if not (1 <= cil_radek <= 8 and 1 <= cil_sloupec <= 8):
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False
    
    if typ == "pěšec":
        return je_tah_mozny_pesec(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "věž":
        return je_tah_mozny_vez(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "střelec":
        return je_tah_mozny_strelec(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "jezdec":
        return je_tah_mozny_jezdec(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "král":
        return je_tah_mozny_kral(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "dáma":
        return je_tah_mozny_dama(pozice, cilova_pozice, obsazene_pozice)
    else:
        return False
    


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True