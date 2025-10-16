def faktorial(n):
    
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

def faktorial2(n):
    vysledek = 1

    if n == 0 or n == 1:
        return 1
    
    for index in range(1, n + 1):
        vysledek *= index

    return vysledek


if __name__ == "__main__":

    print(faktorial(0))
    print(faktorial(1))
    print(faktorial(4))
    print(faktorial(8))

    print(faktorial2(0))
    print(faktorial2(1))
    print(faktorial2(4))
    print(faktorial2(8))