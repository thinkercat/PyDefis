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

valeur_de_fin = 1435
number = 0
code = 0
while number < valeur_de_fin:    
    print(f"{code} + {number}")
    if number % 3 == 0 or number % 5 == 0:
        code += number
    number+=1
    print(f"Number = {number} et Code = {code}\n")

print(code)
