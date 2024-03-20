def cesarova_sifra(text, posun):
    zasifrovany_text = ""
    for znak in text:
        if znak.isalpha():
            velikost_pismene = ord('A') if znak.isupper() else ord('a')
            index = ord(znak) - velikost_pismene
            zasifrovany_index = (index + posun) % 26
            zasifrovany_znak = chr(velikost_pismene + zasifrovany_index)
            zasifrovany_text += zasifrovany_znak
        else:
            zasifrovany_text += znak
    return zasifrovany_text

text = input("Zadejte text k zašifrování: ")
posun = int(input("Zadejte počet posunutí v abecedě: "))
zasifrovany_text = cesarova_sifra(text, posun)

print("Zašifrovaný text:", zasifrovany_text)
