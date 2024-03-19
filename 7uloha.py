def prevod_na_hodiny(dny, hodiny):
    celkovy_cas_v_hodinach = dny * 24 + hodiny
    return celkovy_cas_v_hodinach
dny = int(input("Zadejte počet dnů: "))
hodiny = int(input("Zadejte počet hodin: "))
celkovy_cas_v_hodinach = prevod_na_hodiny(dny, hodiny)
print("Časový údaj", dny, "dnů a", hodiny, "hodin je celkem", celkovy_cas_v_hodinach, "hodin.")
