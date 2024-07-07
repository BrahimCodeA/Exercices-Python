
liste_user = []
choix_user = ""
print("--- Bienvenue dans la liste de courses ---")

while True:
    MENU = input("""
1. Ajouter un produit dans la liste
2. Afficher la liste
3. Supprimer un article de la liste
4. Vider la liste
5. Quitter 
Quel action souhaitez-vous faire ? """)
    if MENU == "1":
        choix_user = input("Quel element souaihtez-vous ajouter ? : ")
        if choix_user in liste_user:
            print(f"{choix_user} fait deja partie de la liste")
        else:
            liste_user.append(choix_user)
            print(f"{choix_user} à bien été ajouté ")
        
    elif MENU == "2":
        print(f"Votre liste : {liste_user}")
        
    elif MENU == "3":
        choix_user = input("Quel element souhaitez-vous supprimer ? : ")
        if choix_user not in liste_user:
            print(f"{choix_user} cette élement n'existe pas dans la liste")
        else:
            liste_user.remove(choix_user)
            print(f"{choix_user} à bien été supprimé")
       
    elif MENU == "4":
        if choix_user not in liste_user:
            print("La liste est deja vide !")
        else:
            liste_user.clear()
            print("La liste à été vidé")
        
    elif MENU == "5":
        print("Vous avez decidé de quitter la liste.")
        break
    
    
