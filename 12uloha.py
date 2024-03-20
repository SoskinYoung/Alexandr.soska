import math
xA, yA = 5, 1
xB, yB = -2, 18
vzdalenost = math.sqrt((xB - xA)**2 + (yB - yA)**2)
print("Vzdálenost mezi body A[{}, {}] a B[{}, {}] je {:.2f}".format(xA, yA, xB, yB, vzdalenost))
