
choix = ["1","2","3","4","5","6"]
terme1 = 0
terme2 = 0
MENU = ""

while MENU not in choix:
    MENU = input("""---- Calculatrice: MENU ----
1 - Addition.
2 - Soustraction.
3 - Multiplication.
4 - Division.
5 - Reste d'une division entiére.
6 - Puissance.
Quel calcul veux-tu effectuer ? """)

    if MENU == "1":
        terme1 = int(input("Entrez le premier terme : "))
        terme2 = int(input("Entrez le deuxiéme terme : "))
        calcul = terme1 + terme2
        print(f"Le resultat de l'addition est : {calcul}")
    elif MENU == "2":
        terme1 = int(input("Entrez le premier terme : "))
        terme2 = int(input("Entrez le deuxiéme terme : "))
        calcul = terme1 - terme2
        print(f"Le resultat de la soustraction est : {calcul}")
    elif MENU == "3":
        terme1 = int(input("Entrez le premier terme : "))
        terme2 = int(input("Entrez le deuxiéme terme : "))
        calcul = terme1 * terme2
        print(f"Le resultat de la multiplication est : {calcul}")
    elif MENU == "4":
        terme1 = int(input("Entrez le premier terme : "))
        terme2 = int(input("Entrez le deuxiéme terme : "))
        calcul = terme1 / terme2
        print(f"Le resultat de la divison est : {calcul}")
    elif MENU == "5":
        terme1 = int(input("Entrez le premier terme : "))
        terme2 = int(input("Entrez le deuxiéme terme : "))
        calcul = terme1 % terme2
        print(f"Le resultat de lu reste est : {calcul}")
    elif MENU == "6":
        terme1 = int(input("Entrez le premier terme : "))
        terme2 = int(input("Entrez le deuxiéme terme : "))
        calcul = terme1 ** terme2
        print(f"Le resultat de la puissance est : {calcul}")
    else:
        print("Vous devez choisir une option entre 1 et 6 ")
    M = input("Souhaitez vous faire un autre clacul (O/N) ? ")
    if M == "O":
        continue
    elif M == "N":
        break

