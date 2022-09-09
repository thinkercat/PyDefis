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
ChauveSouris = 0
Skellington = 0
Zombie = 0
Fantome = 0

creatures = [ChauveSouris,Skellington,Zombie,Fantome]

ChauveSourisDamage = 0
SkellingtonDamage = 0
FantomeDamage = 0

AntonioHit = [ChauveSourisDamage,SkellingtonDamage,FantomeDamage]

TimeSecondes = 0
TimeMin = 0

while TimeMin < 50 :
    TimeSecondes = TimeSecondes + 1     #Symbolise les secondes, 1 seconde = 1
    TimeMin = TimeSecondes / 60     #Symbolise les minutes, 1 minute = 60 / secondes EX: 120secondes : 120/60 = 2minutes
    print("\n",TimeSecondes,"Second","\n",TimeMin,"Minutes","\n")

