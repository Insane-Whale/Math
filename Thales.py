import os




def Triangle_simple():
    print("******************************************************** ")
    print("**************************A***************************** ")
    print("**************************/\\****************************")
    print("*************************/  \\***************************")
    print("************************/    \\**************************")
    print("***********************/      \\*************************")
    print("**********************/        \\************************")
    print("*********************/          \\***********************")
    print("********************/            \\**********************")
    print("*******************/              \\*********************")
    print("******************/                \\********************")
    print("****************D/__________________\\E******************")
    print("****************/                    \\******************")
    print("***************/                      \\*****************")
    print("**************/                        \\****************")
    print("************B/__________________________\\C**************")
    print("******************************************************** ")
    print("******************************************************** ")

def Triangle_double():
    print("***************************************")
    print("**********E________________D***********")
    print("***********\\              %************")
    print("************\\            %*************")
    print("*************\\          %**************")
    print("**************\\        %***************")
    print("***************\\      %****************")
    print("****************\\    %*****************")
    print("*****************\\  %******************")
    print("******************\\%*******************")
    print("*****************A%\\*******************")
    print("*****************%  \\******************")
    print("****************%    \\*****************")
    print("***************%      \\****************")
    print("**************%        \\***************")
    print("*************%          \\**************")
    print("************%            \\*************")
    print("**********B%______________\\C***********")
    print("***************************************")

def Thales():
    os.system("cls")
    choix_methode = ''
    while choix_methode == '':
        print("Que voulez vous calculer :")
        print("[1]-Calculer la longueur d'un coté")
        choix_methode = input(': ')
        # print("[2]- UTILISER LA RECIPROQUE ???")

        if choix_methode == "1":
            os.system("cls")
            choix_configuration = ''
            while choix_configuration == '':
                print("Quelle configuration de Thales voulez vous utiliser: \n[1]-Un seul triangle \n[2]-Deux triangles rejoint par leurs sommet\n")
                choix_configuration = input(": ")
                if choix_configuration == "1":
                    os.system("cls")
                    Triangle_simple()
                    Longueur = ''
                    while Longueur == '':
                        Longueur = input("Quelle longueur cherchez vous : ")
                        if Longueur == 'AB':
                            verif = ''
                            while verif == '':
                                AD = input('Longueur AD: ')
                                AC = input('Longueur AC: ')
                                AE = input('Longueur AE: ')
                                verif = 1
                                try:
                                    try:
                                        AD = int(AD)
                                    except ValueError:
                                        AD = float(AD)
                                    try:
                                        AC = int(AC)
                                    except ValueError:
                                        AC = float(AC)
                                    try:
                                        AE = int(AE)
                                    except ValueError:
                                        AE = float(AE)
                                except:
                                    print("Au moins une des valeurs saisie est invalide")
                                    input("\nAppuyez sur Entrée")
                                    os.system("cls")
                                    Triangle_simple()
                                    print(f"Quelle longueur cherchez vous : {Longueur}")
                                    verif = ''
                                AB = (AD*AC)/AE
                                print(f"La longueur AB est égale a : {AB}")

                        elif Longueur == 'AD':
                            verif= ''
                            while verif == '':
                                AB = input('Longueur AB: ')
                                AC = input('Longueur AC: ')
                                AE = input('Longueur AE: ')
                                verif = 1
                                try:
                                    try:
                                        AB = int(AB)
                                    except ValueError:
                                        AB = float(AB)
                                    try:
                                        AC = int(AC)
                                    except ValueError:
                                        AC = float(AC)
                                    try:
                                        AE = int(AE)
                                    except ValueError:
                                        AE = float(AE)
                                except:
                                    print("Au moins une des valeurs saisie est invalide")
                                    input("\nAppuyez sur Entrée")
                                    os.system("cls")
                                    Triangle_simple()
                                    print(f"Quelle longueur cherchez vous : {Longueur}")
                                    verif = ''
                                AD = (AB*AE)/AC
                                print(f"La longueur AD est égale a : {AD}")

                        elif Longueur == 'AE':
                            verif= ''
                            while verif == '':
                                AB = input('Longueur AB: ')
                                AC = input('Longueur AC: ')
                                AD = input('Longueur AD: ')
                                verif = 1
                                try:
                                    try:
                                        AB = int(AB)
                                    except ValueError:
                                        AB = float(AB)
                                    try:
                                        AC = int(AC)
                                    except ValueError:
                                        AC = float(AC)
                                    try:
                                        AD = int(AD)
                                    except ValueError:
                                        AD = float(AD)
                                except:
                                    print("Au moins une des valeurs saisie est invalide")
                                    input("\nAppuyez sur Entrée")
                                    os.system("cls")
                                    Triangle_simple()
                                    print(f"Quelle longueur cherchez vous : {Longueur}")
                                    verif = ''
                                AE = (AB*AD)/AC
                                print(f"La longueur AE est égale a : {AE}")
                        elif Longueur == 'AC':
                            verif= ''
                            while verif == '':
                                AB = input('Longueur AB: ')
                                AE = input('Longueur AE: ')
                                AD = input('Longueur AD: ')
                                verif = 1
                                try:
                                    try:
                                        AB = int(AB)
                                    except ValueError:
                                        AB = float(AB)
                                    try:
                                        AE = int(AE)
                                    except ValueError:
                                        AE = float(AE)
                                    try:
                                        AD = int(AD)
                                    except ValueError:
                                        AD = float(AD)
                                except:
                                    print("Au moins une des valeurs saisie est invalide")
                                    input("\nAppuyez sur Entrée")
                                    os.system("cls")
                                    Triangle_simple()
                                    print(f"Quelle longueur cherchez vous : {Longueur}")
                                    verif = ''
                                AC = (AB*AD)/AE
                                print(f"La longueur AC est égale a : {AC}")
                        elif Longueur == 'DE':
                            verif= ''
                            while verif == '':
                                AB = input('Longueur AB: ')
                                AE = input('Longueur AE: ')
                                AD = input('Longueur AD: ')
                                verif = 1
                                try:
                                    try:
                                        AB = int(AB)
                                    except ValueError:
                                        AB = float(AB)
                                    try:
                                        AE = int(AE)
                                    except ValueError:
                                        AE = float(AE)
                                    try:
                                        AD = int(AD)
                                    except ValueError:
                                        AD = float(AD)
                                except:
                                    print("Au moins une des valeurs saisie est invalide")
                                    input("\nAppuyez sur Entrée")
                                    os.system("cls")
                                    Triangle_simple()
                                    print(f"Quelle longueur cherchez vous : {Longueur}")
                                    verif = ''
                                AC = (AB*AD)/AE
                                print(f"La longueur AC est égale a : {AC}")
                        elif Longueur == 'BC':
                            pass
                        else:
                            print("Veuillez saisir AB,AD,AE,AC,DE ou BC ")
                elif choix_configuration == "2":
                    pass

                else:
                    print("\nVeuillez saisir 1 ou 2\n")

                    choix_configuration = ''

if __name__ == '__main__':
    Triangle_double()
    Triangle_simple()
    # Thales()