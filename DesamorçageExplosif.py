#!/usr/bin/python
#By https://github.com/thinkercat
#Désamorçage d'un explosif
#https://pydefis.callicode.fr/defis/Desamorcage01/txt

numero_de_série = "797114"
U = int(numero_de_série[0:3])
N = int(numero_de_série[3:6])
print(f"U = {U} et N = {N}")
for n in range(N):
    U*=13
    U = str(U)
    U = int(U[-3:])
print(f"Solution : {U}")
