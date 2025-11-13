from muj_modul import fibonaci
import random

if __name__ == "__main__":
    #fib = fibonaci(10)
    #print(list(reversed(fib)))

    symboly = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    #random.seed(10)

    steps = 0
    while True:
        steps += 1
        vysledek = []
        for i in range(3):
            vysledek.append(random.choice(symboly))
        print(vysledek)
        if len(set(vysledek)) == 1:
            print(f"VYHRÁL JSI po {steps} pokusech!!")
            break