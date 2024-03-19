def desitkova_na_dvojkovou(cislo):
    dvojkova = ""
    while cislo > 0:
        zbytek = cislo % 2
        dvojkova = str(zbytek) + dvojkova
        cislo //= 2
    return dvojkova

cislo_desitkova = int(input("Zadejte číslo v desítkové soustavě: "))
cislo_dvojkova = desitkova_na_dvojkovou(cislo_desitkova)
print("Číslo", cislo_desitkova, "v dvojkové soustavě je:", cislo_dvojkova)