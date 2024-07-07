import random

n = random.randint(1, 30)
print("J'ai choisi un nombre entre 1 et 30 . A vous de le deviner en 5 tentatives au maximum")
nbr_essaie = 5

while nbr_essaie != 0:
    nbr_essaie -= 1
    user_choix = int(input("Quel est le nombre ? : "))
    if user_choix > n:
        print("C'est moins")
        print(f"Il vous reste {nbr_essaie} essaies")
    elif user_choix < n:
        print("C'est plus")
        print(f"Il vous reste {nbr_essaie} essaies")
    else:
        print(f"Bien joué vous avez trouvé en {5 - nbr_essaie} essaies le nombre etait bien {n} ")  
        break
        
else:
    print(f"Dommage {n} etait le bon nombre")


 


       
        
    