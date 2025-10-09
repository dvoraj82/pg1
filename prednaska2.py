if __name__ == "__main__":


    hodnota1 = input("zadej cislo: ")
    hodnota1 = int(hodnota1)

    operator = input("Zadej operator (+, -, *, /): ")

    hodnota2 = input("Zadej druhe cislo: ")
    hodnota2 = int(hodnota2)

    #print(hodnota1, operator, hodnota2)
    #print(f"Operace: {hodnota1} {operator} {hodnota2} = ")

    vysledek = None
    
    if operator == "+":
        vysledek = hodnota1 + hodnota2
    elif operator == "-":
        vysledek = hodnota1 - hodnota2
    elif operator == "*":
        vysledek = hodnota1 * hodnota2
    elif operator == "/":
        if hodnota2 == 0:
            print("Nelze dělit nulou!")
        else:
            vysledek = hodnota1 / hodnota2
    else:
        print(f"Neznámí operátor: {operator}")
    

    if vysledek is None:
        print("Operace se nevydařila")
    else:
        print(f"Vysledek operace je: {vysledek}")
