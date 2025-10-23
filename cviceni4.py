def jaccardova_vzdalenost_mnozin(mnozina1, mnozina2):
    """
    Jaccardova vzdalenost říká, jak jsou dvě množiny rozdílné 0 znamená, že jsou stejné, 1 znamená, že jsou zcela rozdílné
    """
    mnozina1 = set(mnozina1)
    mnozina2 = set(mnozina2)

    prunik = mnozina1.intersection(mnozina2)
    sjednoceni = mnozina1.union(mnozina2)

    jindex =  len(prunik) / len(sjednoceni)

    return 1 - jindex

def levensteinova_vzdalenost(dotaz1, dotaz2): #pomocí while
    """
    Levensteinova vzdalenost říka, jak jsou 2 řetězce rozdílné, pokud jsou stejné je Levensteinova vzdalenost 0,
    pro řetězce "čas" a "čaj" je Levensteinova vzdalenost 1 (liší se v 1 písmenu)
    """
    delka = max(len(dotaz1), len(dotaz2))
    i = 0
    lev = 0

    while i < delka:
        if i < len(dotaz1) and i < len(dotaz2):
            if dotaz1[i] != dotaz2[i]:
                lev += 1
        else:
            lev += 1
        
        i += 1

    return lev

def levensteinova_vzdalenost_for(dotaz1, dotaz2): #pomocí for
    
    lev = 0
    delka = min(len(dotaz1), len(dotaz2))

    for i in range(delka):
        if dotaz1[i] != dotaz2[i]:
            lev += 1
    lev += abs(len(dotaz1) - len(dotaz2))

    return lev


if __name__ == "__main__":

    serp1 = ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    serp2 = ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    serp3 = ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]

    print(jaccardova_vzdalenost_mnozin(serp1, serp2))
    print(jaccardova_vzdalenost_mnozin(serp2, serp3))
    print(jaccardova_vzdalenost_mnozin(serp1, serp3))

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    print(levensteinova_vzdalenost_for(query1, query2))
    print(levensteinova_vzdalenost_for(query2, query3))
    print(levensteinova_vzdalenost_for(query1, query3))
    print(levensteinova_vzdalenost_for(query1, query4))

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))
    print(levensteinova_vzdalenost(query1, query4))