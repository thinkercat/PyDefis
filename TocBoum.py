#!/usr/bin/python
#By https://github.com/thinkercat
#PyDéfis
#Toc Boum
#https://pydefis.callicode.fr/defis/TocBoum/txt

# nombre = 13*a+7*b

essai = 1000
nombre = 3188
dif_min = 1000
couples = []

for a in range(essai):
    for b in range(essai):
            b += 1
            if 13*a+7*b == nombre:
                dif = abs(a-b)
                if dif < dif_min:
                    dif_min = dif
                    couple = [a,b]
    a += 1

print(couple, dif_min)
