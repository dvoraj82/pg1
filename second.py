def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    
    cislo = int(cislo)

    jednotky = [
        "nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"
    ]

    nactiny = [
        "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"
    ]

    desitky = [
        "", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"
    ]

    if cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return nactiny[cislo - 10]
    elif cislo == 100:
        return "sto"
    else:
        des = cislo // 10
        jed = cislo % 10
        if jed == 0:
            return desitky[des]
        else:
            return desitky[des] + " " + jednotky[jed]

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)