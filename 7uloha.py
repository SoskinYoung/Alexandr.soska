def vypis_interval(a, b):
    for i in range(a, b + 1):
        print(i, end="")
        if i < b:
            print(", ", end="")
    print()
a = int(input("Zadejte počáteční hodnotu intervalu: "))
b = int(input("Zadejte koncovou hodnotu intervalu: "))

print("Čísla v intervalu <" + str(a) + ";" + str(b) + ">: ", end="")
vypis_interval(a, b)