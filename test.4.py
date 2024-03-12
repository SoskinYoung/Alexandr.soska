def cezarova_sifra(text, posun):
    zasifrovany_text = ""

    for znak in text:
        # Kontrola, zda je znak písmeno
        if znak.isalpha():
            # Určení velikosti písmene (velké/malé)
            velke_pismeno = znak.isupper()
            
            # Převedení písmene na číslo v rozmezí 0-25
            cislo = ord(znak) - ord('A') if velke_pismeno else ord(znak) - ord('a')
            
            # Aplikace posunu
            cislo = (cislo + posun) % 26
            
            # Převedení čísla zpět na písmeno
            novy_znak = chr(cislo + ord('A')) if velke_pismeno else chr(cislo + ord('a'))
            
            # Přidání nového znaku k zašifrovanému textu
            zasifrovany_text += novy_znak
        else:
            # Pokud není znak písmeno, ponecháme ho beze změny
            zasifrovany_text += znak

    return zasifrovany_text

# Příklad použití
text_ke_zasifrovani = "Ahoj Zmrde!"
posun = 10
zasifrovany_text = cezarova_sifra(text_ke_zasifrovani, posun)

print(f"Text: {text_ke_zasifrovani}")
print(f"Zašifrovaný text: {zasifrovany_text}")
