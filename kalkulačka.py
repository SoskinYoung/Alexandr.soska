def programuj_jednoduse():
    print("Vítejte v jednoduchém programu pro počítání!")
    cislo1 = float(input("Zadejte první číslo: "))
    cislo2 = float(input("Zadejte druhé číslo: "))
    print("Výsledky operací:")
    print("Sčítání:", cislo1 + cislo2)
    print("Odčítání:", cislo1 - cislo2)
    print("Násobení:", cislo1 * cislo2)
    if cislo2 != 0:
        print("Dělení:", cislo1 / cislo2)
    else:
        print("Dělení: Nelze dělit nulou!")
