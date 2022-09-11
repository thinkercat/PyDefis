#!/usr/bin/python
#By https://github.com/thinkercat
#PyDéfis
#SW IV : On passe en vitesse lumière
#https://pydefis.callicode.fr/defis/VitesseLumiere/txt

## Enoncé ##
# initialiser x, y, et z
# tant que 10 * x > y :
#     x = (y * z) % 10000
#     y = (3 * z) % 10000
#     z = (7 * z) % 10000 
# afficher les navi-composantes : x, y, z

# Script #
x = 997
y = 312 
z = 663 

while 10 * x > y :
    x = (y*z)%10000
    y = (3*z)%10000
    z = (7*z)%10000

print(x,y,z)