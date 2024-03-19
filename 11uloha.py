def zbytek_po_deleni(delenec, delitel):
    while delenec >= delitel:
        delenec -= delitel
    return delenec
delenec = int(input("Zadejte dělenec: "))
delitel = int(input("Zadejte dělitel: "))
zbytek = zbytek_po_deleni(delenec, delitel)
print("Zbytek po dělení", delenec, "číslem", delitel, "je", zbytek)
