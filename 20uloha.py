import random
pole = [random.randint(1, 100) for _ in range(10)]
print("Náhodná čísla v poli:")
for prvek in pole:
    print(prvek)
nejmensi = min(pole)
nejvetsi = max(pole)
prumer = sum(pole) / len(pole)
print("\nNejmenší hodnota v poli je:", nejmensi)
print("Největší hodnota v poli je:", nejvetsi)
print("Průměrná hodnota v poli je:", prumer)
