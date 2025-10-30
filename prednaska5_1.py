import sys

if __name__ == "__main__":

    try:
        name = input("Zadej jmeno souboru k nacteni: ")
        file = open(name, "r")
        data = file.readline().strip()
        print(data)
        data = file.readline()
        print(data)

        file.close()
    
    except FileNotFoundError as e:
        print(f"Soubor {name} neexistuje!")