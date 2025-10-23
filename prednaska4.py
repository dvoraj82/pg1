def vrat_3_hodnoty():
    return 3, 6, 9




if __name__ == "__main__":

    prvni, druhy, treti = vrat_3_hodnoty()
    print(prvni)
    print(druhy)
    print(treti)

    student = {
        "name": "Alice",
        "age": 25
    }

    print(student)


    fronta = [] #FIFO
    fronta.append(10)
    fronta.append(5)
    fronta.append(1)
    fronta.append(20)


    print(fronta.pop(0))

    fronta.append(3)

    print(fronta.pop(0))
    print(fronta.pop(0))
    print(fronta.pop(0))
    print(fronta.pop(0))


    zasobnik = [] #LIFO
    zasobnik.append(10)
    zasobnik.append(5)
    zasobnik.append(1)
    zasobnik.append(20)

    print(zasobnik.pop())

    zasobnik.append(3)

    print(zasobnik.pop())
    print(zasobnik.pop())
    print(zasobnik.pop())
    print(zasobnik.pop())