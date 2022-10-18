#!/usr/bin/python
#By https://github.com/thinkercat
#PyDéfis
#LunettesAstro
#https://pydefis.callicode.fr/defis/LunetteAstro/txt

x = 1694
y = 1546
iteration = 50
for n in range(iteration):
    x2 = (x + 2 * y) % 2018
    y2 = (y + x * -3) % 2018
    x = x2
    y = y2

declinaison = (x-900) /10
ascensiondroite = (y / 150) *2

print(f"Déclinaison et ascensiondroite : {declinaison},{ascensiondroite}")