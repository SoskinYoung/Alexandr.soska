print("Vitej v kalkulačce na vypočtu platbach" )
cena = int(input("kolik mate zaplatit? "))
tip = int(input("kolik chcete dat díško v % "))
lidi = int(input("mezi kolika lidi se rozdelite časku "))

první_pladba = int(cena + (cena * tip / 100)) / lidi

print int((f"kazdí človek zaplatí {první_pladba} Kč"))