import math
prumer_zeme_km = 6371
prumer_slunce_km = 696340
objem_zeme = (4/3) * math.pi * (prumer_zeme_km / 2)**3
objem_slunce = (4/3) * math.pi * (prumer_slunce_km / 2)**3
povrch_zeme = 4 * math.pi * (prumer_zeme_km / 2)**2
povrch_slunce = 4 * math.pi * (prumer_slunce_km / 2)**2
kolikrat_vejde_zeme_do_slunce = objem_slunce / objem_zeme
kolik_zemi_na_obvod_slunce = prumer_slunce_km / (2 * prumer_zeme_km)
print("Objem Země:", objem_zeme, "km^3")
print("Objem Slunce:", objem_slunce, "km^3")
print("Povrch Země:", povrch_zeme, "km^2")
print("Povrch Slunce:", povrch_slunce, "km^2")
print("Kolikrát se vejde Země do Slunce:", kolikrat_vejde_zeme_do_slunce)
print("Kolik Zemí je potřeba jako korálky po obvodu Slunce:", kolik_zemi_na_obvod_slunce)
