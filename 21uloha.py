import random
pole = [random.randint(1, 100) for _ in range(10)]
print("Původní pole:")
print(pole)
seřazené_pole = sorted(pole)
print("\nSeřazené pole:")
print(seřazené_pole)
