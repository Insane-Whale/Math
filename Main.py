import math
import cmath
import matplotlib 
from Pythagore import Pythagore

print("bienvenue dans ce logiciel de calcul scientifique")

choix = ''

while choix == '':
    print("Quel operation souhaitez vous effectuer :")
    print("[1]- Pythagore")


    choix = input(": ")

    if choix == "1":
        Pythagore()


    else:
        print("Veuillez choisir un chiffre valide")
        choix = ''