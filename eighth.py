def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    vysledek = 0
    mocnina = 0

    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)
    
    for cifra in reversed(binarni_cislo):
        if cifra not in ("0", "1"):
            raise ValueError("Vstup neni validni binarni cislo!!")
        
        vysledek += int(cifra) * (2 ** mocnina)
        mocnina += 1
        
    return vysledek


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128