def vypocet_rustu_uspor(počatecni_vklad, urokova_mira, doba_uspor):
    konecna_castka = počatecni_vklad * (1 + urokova_mira / 100 * doba_uspor)
    rust_uspor = konecna_castka - počatecni_vklad
    return rust_uspor
počatecni_vklad = float(input("Zadejte počáteční vklad (v Kč): "))
urokova_mira = float(input("Zadejte roční úrokovou míru (v %): "))
doba_uspor = float(input("Zadejte dobu úspor (v letech): "))

rust_uspor = vypocet_rustu_uspor(počatecni_vklad, urokova_mira, doba_uspor)
print("Vaše úspory vzrostou o {:.2f} Kč.".format(rust_uspor))

