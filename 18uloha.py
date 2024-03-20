def ciferny_soucet(cislo):
    soucet = 0
    while cislo > 0:
        soucet += cislo % 10
        cislo //= 10  
    return soucet
cislo = int(input("Zadejte přirozené číslo: "))
vysledek = ciferny_soucet(cislo)
print("Ciferný součet čísla", cislo, "je", vysledek)
