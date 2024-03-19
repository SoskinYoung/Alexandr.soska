def je_prvocislo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def vypis_prvocisla(do_cisla):
    print("Prvočísla do", do_cisla, "jsou:")
    for number in range(2, do_cisla + 1):
        if je_prvocislo(number):
            print(number, end=" ")
n = int(input("Zadejte číslo n: "))
