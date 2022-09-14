#!/usr/bin/python
#By https://github.com/thinkercat
#Désamorçage à la Tony Stark
#https://pydefis.callicode.fr/defis/SpymasterBomb/txt

# Tout ce dont il se souvient, c'est que le code à entrer est la 
# somme de tous les nombres qui sont multiples de 3 ou de 5, et 
# qui sont strictement inférieurs à un autre nombre. Cet autre 
# nombre, gravé sur la bombe, est donné en entrée du problème.

# Exemple
# Si le nombre gravé sur la bombe avait été 20, le code aurait été 78 :
# 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18

# Valeur : 1435
## Scipt ##

valeur = 1435
Rvaleur = 1
Qvaleur = 1
print("1")
while Rvaleur != 0 :
    if valeur%3 == 0 :
        Rvaleur = valeur%3
        Qvaleur = valeur//3
        print(Rvaleur,Qvaleur)
    elif valeur%5 == 0:
        Rvaleur = valeur%3
        Qvaleur = valeur//3
        print(Rvaleur,Qvaleur)
    valeur -= Qvaleur
    print(valeur)
print("2")