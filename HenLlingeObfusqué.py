#!/usr/bin/python
#By https://github.com/thinkercat
#PyDéfis
#Hen Llinge obfusqué
#https://pydefis.callicode.fr/defis/C22_Obfuscate01/txt

##############################
#   SOLUTION : Minnea Enid -> Aimer Paqueretes
##############################

# Chaine de characteres à déchiffrer : en Supprimant les minuscules suivis de la meme majuscule (eE,xX)
# ccChjJaaAticCIuU -> chat
# 0123456789
# MzZfiIFmMpPizwWZkbByYKfFjJkKusSbBUplLqisSlLdDIQPnrRnuUuU
# sgkKfFdDGSxhHmMmMXgGjaAJpzZpeEPPnNpncmMinNIwpPWfFcCCNPnq
# QxXNeqQhHraefFEdkKDpmMPARaqQqQikjJKmMoOIrRpPoOnNmyYMfFxX
# koOsSKzZwefFEWvV yYyYjJpPEviIzeExXZxgGwWjkKJXmMxXVvVkqQo
# OagxXGeEAoOpPtTntTNnNKjtTxXwWgGJunjJdDoONUspPSutTtgGTUhH
# qlLrRQmuUjJnwfFWNxXpzZPyYlLzZMoOnweEfFWkwpPjJWnNxXKyYjJy
# YfFuUicbBCcCpuUoOPoeEoOsgwWsaAsSSjJGkKeEnNSpPvVsmyYMoOsS
# SOxXdyqQzZmMmMYnNDd

# CODE


from glob import glob
from xml.etree.ElementPath import find



def decrypt(str):

    #Variables
    Filtre = ["aA","bB","cC","dD","eE",
            "fF","gG","hH","iI","jJ",
            "kK","lL","mM","nN","oO",
            "pP","qQ","rR","sS","tT",
            "uU","vV","wW","xX","yY","zZ"]

    MotChiffre = Mot
    essai = 0
    a = 0
    
    while a != 5:   # Permet de répéter l'operation x fois
        a = a + 1

        for i in Filtre:     # Permet de supprimer les Filtres          
            essai = essai +1
            print("ESSAI : ", essai)

            MotChiffre = MotChiffre.split(i)
            MotChiffre = "".join(MotChiffre)

            print(MotChiffre)
            
    
    print("Solution :", MotChiffre) #Renvoie la solution
    

Mot = "MzZfiIFmMpPizwWZkbByYKfFjJkKusSbBUplLqisSlLdDIQPnrRnuUuUsgkKfFdDGSxhHmMmMXgGjaAJpzZpeEPPnNpncmMinNIwpPWfFcCCNPnqQxXNeqQhHraefFEdkKDpmMPARaqQqQikjJKmMoOIrRpPoOnNmyYMfFxXkoOsSKzZwefFEWvV yYyYjJpPEviIzeExXZxgGwWjkKJXmMxXVvVkqQoOagxXGeEAoOpPtTntTNnNKjtTxXwWgGJunjJdDoONUspPSutTtgGTUhHqlLrRQmuUjJnwfFWNxXpzZPyYlLzZMoOnweEfFWkwpPjJWnNxXKyYjJyYfFuUicbBCcCpuUoOPoeEoOsgwWsaAsSSjJGkKeEnNSpPvVsmyYMoOsSSOxXdyqQzZmMmMYnNDd"

decrypt(Mot)


