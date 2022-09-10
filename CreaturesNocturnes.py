#!/usr/bin/python
#By https://github.com/thinkercat
#PyDéfis
#Créatures Nocturnes
#https://pydefis.callicode.fr/defis/C22_VampireSurvivors/txt

# Au démarrage du jeu, il n'y a aucune créature ;
# 10 chauves-souris apparaissent toutes les 2 secondes ;
# 5 skellingtons apparaissent toutes les 5 secondes ;
# 4 zombies apparaissent toutes les 6 secondes ;
# 3 fantômes baveux apparaissent toutes les 10 secondes.

# Durant les quatre premières minutes de jeu il faut à Antonio :
# 6 secondes pour tuer 2 chauves-souris ;
# 20 secondes pour tuer 1 skellington ;
# 30 secondes pour tuer 1 zombie ;
# 40 secondes pour tuer 1 fantôme baveux.

# Toutes les quatre minutes Antonio va s'améliorer, et dans le même temps, il pourra 
# tuer 2 chauves-souris, 1 skellington, 1 zombie et 1 fantôme baveux supplémentaires.

#Variables au démarrage du jeu

# Creatures
ChauveSouris = 0
Skellington = 0
Zombie = 0
Fantome = 0

# Damage
ChauveSourisDamage = 0
SkellingtonDamage = 0
ZombieDamage = 0
FantomeDamage = 0

# Time
TimeSecondes = 0
TimeMin = 0

# Deroulement de la partie
while TimeMin < 50 :    # La partie dure 50min
    TimeSecondes = TimeSecondes + 1     #Symbolise les secondes, 1 seconde = 1
    TimeMin = TimeSecondes / 60     #Symbolise les minutes, 1 minute = 60 / secondes EX: 120secondes : 120/60 = 2minutes
#    print("\n",TimeSecondes,"Second","\n",TimeMin,"Minutes") #Montre le resultat à chaque secondes

    # Apparition des créatures par tours
    if TimeSecondes%2 == 0 :                # Chaque 2s 
        ChauveSouris = ChauveSouris + 10    # ChauveSouris Augmente de 10

    if TimeSecondes%5 == 0 :                # Chaque 5s
        Skellington = Skellington + 5       # Skellington Augmente de 5

    if TimeSecondes%6 == 0 :                # Chaque 6s
        Zombie = Zombie + 4                 # Zombie Augmente de 4

    if TimeSecondes%10 == 0 :               # Chaque 10s
        Fantome = Fantome + 3               # Fantome Augmente de 3

    # Amelioration Antonio
    if TimeMin%4 == 0 :                                 # Chaque 4min
        ChauveSourisDamage = ChauveSourisDamage + 2     # ChauveSourisDamage Augmente de 2
        SkellingtonDamage = SkellingtonDamage + 1       # SkellingtonDamage Augmente de 1
        ZombieDamage = ZombieDamage + 1                 # ZombieDamage Augmente de 1
        FantomeDamage = FantomeDamage + 1               # FantomeDamage Augmente de 1

    # Dégats par tours
    if TimeSecondes%6 == 0:                                 # Chaque 6s
        ChauveSouris = ChauveSouris - ChauveSourisDamage    # ChauveSourisDamage Diminue de ChauveSourisDamage
    
    if TimeSecondes%20 == 0 :                               # Chaque 20s
        Skellington = Skellington - SkellingtonDamage       # SkellingtonDamage Diminue de SkellingtonDamage
    
    if TimeSecondes%30 == 0 :                               # Chaque 30s
        Zombie = Zombie - ZombieDamage                      # ZombieDamage Diminue de ZombieDamage
    
    if TimeSecondes%40 == 0 :                               # Chaque 40s
        Fantome = Fantome - FantomeDamage                   # FantomeDamage Diminue de FantomeDamage

    if TimeMin%1 == 0 :
        print(TimeMin,"Min  ",ChauveSouris,Skellington,Zombie,Fantome)
#    print("**Créatures**\nChauves souris: ",ChauveSouris,"\nSkellingtons: ",Skellington,"\nZombies: ",Zombie,"\nFantomes: ",Fantome)
#    print("**Dégats**\nChauves souris:",ChauveSourisDamage,"\nSkellingtons: ",SkellingtonDamage,"\nZombies: ",ZombieDamage,"\nFantomes: ",FantomeDamage)

print("RESULT:",ChauveSouris,Skellington,Zombie,Fantome)
