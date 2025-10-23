from cviceni4 import jaccardova_vzdalenost_mnozin
from cviceni4 import levensteinova_vzdalenost

def duplikace_dotazu_while(dotazy):
    i = 0
    while i < len(dotazy):
        j = i + 1
        while j < len(dotazy):
            jaccard = jaccardova_vzdalenost_mnozin(dotazy[i]["serp"], dotazy[j]["serp"])
            levenstein = levensteinova_vzdalenost(dotazy[i]["dotaz"], dotazy[j]["dotaz"])
            if jaccard < 0.5:
                print(f"Odstraň dotazy {dotazy[j]["dotaz"] } kvůli jaccardově vzdálenosti {jaccard}")
            elif levenstein <= 1:
                print(f"Odstraň dotazy {dotazy[j]["dotaz"] } kvůli jaccardově vzdálenosti {levenstein}")
            if jaccard < 0.5 or levenstein <= 1:
                dotazy.pop(j)
            else: j += 1
        i += 1
    return dotazy

def duplikace_dotazu_for(dotazy):

    results = [dotazy.pop(0)]

    for dotaz1 in dotazy:
        remove = False
        for dotaz2 in results:
            jaccard = jaccardova_vzdalenost_mnozin(dotaz1["serp"], dotaz2["serp"])
            levenstein = levensteinova_vzdalenost(dotaz1["dotaz"], dotaz2["dotaz"])
            if jaccard < 0.5 or levenstein <= 1:
                remove = True
        if not remove:
            results.append(dotaz1)
    return results

if __name__ == "__main__":
        
    dotaz1 = {
        "dotaz": "seznam",
        "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    dotaz4 = {
        "dotaz": "google",
        "serp": ["https://www.google.com", "https://maps.google.com", "https://www.gmail.com"]
    }
    print(duplikace_dotazu_while([dotaz1, dotaz2, dotaz3, dotaz4]))