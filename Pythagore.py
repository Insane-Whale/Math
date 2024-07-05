import os
import math


def pyth_hyp(L1, L2):
    return math.sqrt((L1*L1)+(L2*L2))


def Pythagore():
    while True:    
        os.system("cls")
        print("Bienvenu dans la section Pythagore,\n\nQue voulez vous faire: ")
        print('[1]-Verifier une égalitée')
        print("[2]-Touver la longeur d'un coté")
        choix = input(": ")
        
        if choix == "1":
            os.system("cls")
            verif = 0
            while verif == 0:
                Hypotenuse = input("\n\nRentrez la valeur de l'hypoténuse : ")
                Cote1 = input("Rentrez la valeur d'un des cotés : ")
                Cote2 = input("Rentrez la valeur de l'autre coté : ")
                try :
                    try:
                        Hypotenuse = int(Hypotenuse)
                    except ValueError:
                        Hypotenuse = float(Hypotenuse)

                    try:
                        Cote1 = int(Cote1)
                    except ValueError:
                        Cote1 = float(Cote1)
                    
                    try:
                        Cote2 = int(Cote2)
                    except ValueError:
                        Cote2 = float(Cote2)
                    
                    verif = 1
                except:
                    print("\nveuillez rentrer des chifres valide")
            
            Hyp = pyth_hyp(Cote1, Cote2)
            if  Hyp == Hypotenuse:
                print("\nL'égalitée de pythagore est verifié, votre triangle est rectangle ")
                print(f"Hypoténuse rentrée : {Hypotenuse}")
                print(f"Hypoténuse trouvée : {Hyp}")
                input("Entrée pour continuer")
                os.system("cls")
                
            else :
                print("\nL'égalitée de pythagore n'est pas verifiée, votre triangle n'est pas rectangle")
                print(f"Hypoténuse rentrée : {Hypotenuse}")
                print(f"Hypoténuse trouvée : {Hyp}")
                input("Entrée pour continuer")
                os.system("cls")

        elif choix == "2":
            os.system("cls")
            verif = 0
            while verif == 0:
                print("Voulez vous :\n[1]-Calculer l'Hypoténuse\n[2]-Calculer un coté")
                choix = input(": ")
                if choix == "1":
                    verif2 = ''
                    while verif2 == '':
                        os.system("cls")
                        Cote1 = input("Rentrez la valeur d'un des cotés : ")
                        Cote2 = input("Rentrez la valeur de l'autre coté : ")
                        try :
                            try:
                                Cote1 = int(Cote1)
                            except ValueError:
                                Cote1 = float(Cote1)

                            try:
                                Cote2 = int(Cote2)
                            except ValueError:
                                Cote2 = float(Cote2)
                            
                        except:
                            print("\nveuillez rentrer des chifres valide")
                            

                        Hypotenuse = pyth_hyp(Cote1,Cote2)
                        print(f"La longueur de l'hypothénuse est :{Hypotenuse}")
                        input("Entrée pour continuer")
                        os.system("cls")
                        verif2 = 1
                    verif = 1
                elif choix == "2":
                    os.system("cls")
                    Hypotenuse = input("Rentrez la valeur de l'hypoténuse : ")
                    Cote1 = input("Rentrez la valeur de l'autre coté : ")
                    try :
                        Hypotenuse = int(Hypotenuse)
                        Cote1 = int(Cote1)
                    except ValueError:
                        print("\nveuillez rentrer des chifres valide")
                    Cote2 = math.sqrt((Hypotenuse*Hypotenuse)-(Cote1*Cote1))
                    print(f"La longueur de votre coté est : {Cote2}")
                    input("Entrée pour continuer")
                    os.system("cls")
                    verif = 1
                else:
                    print("Veuillez saisir 1 ou 2\n")
                    verif =0
            
            


if __name__ == '__main__':
    Pythagore()
