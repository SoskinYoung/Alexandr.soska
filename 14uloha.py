R1 = float(input("Zadejte hodnotu odporu R1 v Ohmech: "))
R2 = float(input("Zadejte hodnotu odporu R2 v Ohmech: "))
R_serie = R1 + R2
R_paralelne = 1 / (1/R1 + 1/R2)
print("Celkový odpor zapojení v sérii je", R_serie, "Ohmů.")
print("Celkový odpor zapojení v paralelním spojení je", R_paralelne, "Ohmů.")
