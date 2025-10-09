def prace_se_seznamem1():
    seznam = [100, 5, 3, 21]

    seznam[2] *= 2

    seznam.append(12)

    seznam.sort()
    seznam.reverse()
    
    print(seznam)
    print(seznam[2])

def prace_se_seznamem2(seznam):
    if len(seznam) >= 3:
        return seznam[2]
    else: 
        return None
    
def prumer(cislo):
    return sum(cislo)/len(cislo)

def naformatuj_txt(zak):
    jmeno = zak["jmeno"]
    prijmeni = zak["prijmeni"]
    vek = zak["vek"]
    obor = zak["obor"]
    znamky = zak["znamky"]
    prumer_znamky = round(prumer(znamky), 2)

    text = f"Student: {jmeno} {prijmeni}, Vek: {vek}, Obor {obor}, Prumer: {prumer_znamky}"
    return text

if __name__ == "__main__":
    #prace_se_seznamem1()
    #x = [1,2]
    #print(prace_se_seznamem2(x))
    #y = [12,34,56,78]
    #print(prace_se_seznamem2(y))

    #cisla = [1,2,3,4,5]
    #print(prumer(cisla))

    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1,2,3,1,2,1]
    }

    student["vek"] += 1
    student["obor"] = "AEFP"
    
    print (student["znamky"][2])
    print (student["vek"])

    print(naformatuj_txt(student))