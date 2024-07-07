import random

print("--- Bienvenue dans le jeu du nombre Mystére ---")

nombre_mystere = random.randint(1, 30)
nombre_essaie = 5

while nombre_essaie > 0:
    try:
        user = int(input("Quel nombre choisissez vous ? : "))
        if user < 1 or user > 30:
            print("Veuillez entrer un nombre entre 1 et 30")
            continue
    except ValueError:
        print("Veuillez entrer un nombre ")
        continue
            
    if user < nombre_mystere:
        print(f"C'est plus que {user} ")
        nombre_essaie -= 1
        print(f"Il vous reste {nombre_essaie} essaies")
    elif user > nombre_mystere:
        print(f"C'est moins que {user} ")
        nombre_essaie -= 1
        print(f"Il vous reste {nombre_essaie} essaies ")
    else:
        print(f"Félicitation vous avez trouvé le nombre était bien {user} vous l'avez trouvé en {5 - nombre_essaie + 1} essaies")
        break
        
    if nombre_essaie == 0:
        print(f"Perdu vous n'avez plus d'eesaie, le nombre était {nombre_mystere} ")
        break
    
print("Fin du jeu !")