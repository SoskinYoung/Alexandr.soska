def lezi_na_prime(x, y):
    if 3*x + 2*y - 3 == 0:
        return True
    else:
        return False
x = float(input("Zadejte souřadnici x bodu A: "))
y = float(input("Zadejte souřadnici y bodu A: "))
if lezi_na_prime(x, y):
    print("Bod A[{}, {}] leží na přímce.".format(x, y))
else:
    print("Bod A[{}, {}] neleží na přímce.".format(x, y))
  
