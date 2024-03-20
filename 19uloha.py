import random
pole = [random.randint(1, 100) for _ in range(10)]
print("Náhodná čísla v poli:")
for prvek in pole:
    print(prvek)
