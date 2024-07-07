import random

print("--- Bienvenue dans le jeu de rôle un combat entre Naruto et Sasuke , vous êtes Naruto ---")
naruto = 50
sasuke = 50
nbr_potion = 3

while (naruto >= 0) and (sasuke >= 0):
    choix_user = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    if choix_user == "1":
        naruto_attack = random.randint(5, 10)
        sasuke_attack = random.randint(5, 15)
        print(f"Vous avez infligé {naruto_attack} points de dégats à l'ennemi ")
        print(f"L'ennemi vous a infligé {sasuke_attack}  points de dégats ")
        sasuke -= naruto_attack
        naruto -= sasuke_attack
        print(f"Il vous reste {naruto} point de points de vie.")
        print(f"Il reste {sasuke} point de vie a l'ennemi.")
    
    elif choix_user == "2":
        if nbr_potion > 0:
            potion = random.randint(15, 50)
            naruto += potion
            nbr_potion -= 1
            print(f"Vous avez récupéré {potion} points de vie. ({nbr_potion} potions restantes)")
        else:
            print("Vous n'avez plus de potion.")
            continue  # Passe au prochain tour sans que Naruto attaque ou Sasuke subisse de dégâts
    
    sasuke_attack = random.randint(5, 15)
    naruto -= sasuke_attack
    print("-" * 50)
    print(f"L'ennemi vous a infligé {sasuke_attack} points de dégâts.")
        
    
    print("-" * 50)
print("Fin du jeu !")
        
