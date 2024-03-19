def je_trojuhelnik(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
a = float(input("Zadejte délku strany a: "))
b = float(input("Zadejte délku strany b: "))
c = float(input("Zadejte délku strany c: "))
if je_trojuhelnik(a, b, c):
    print("Zadané délky stran tvoří trojúhelník.")
else:
    print("Zadané délky stran netvoří trojúhelník.")