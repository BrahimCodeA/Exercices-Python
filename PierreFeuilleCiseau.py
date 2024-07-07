import random


ali = ""
score_ordi = 0
score_ali = 0
egalite = 0



while True:
    ordi = random.randint(1,3)
    ali = input("Quel choix (p), (f), (c) (q)? ")
    
    if ali == "q":
        print("Fin du jeu !")
        print(f"Score Ali {score_ali}")
        print(f"Score ordi {score_ordi}")
        break
    
    if ali == "p" and ordi == 2:
        score_ordi += 1
        print(f"Le score de l'ordi est : {score_ordi}")
        
    elif ali == "p" and ordi == 1:
           egalite += 1
           print("egalite")
        
    elif ali == "p" and ordi == 3:
        print(f"Le score de Ali est : {score_ali}")
        score_ali += 1
        
    elif ali == "f" and ordi == 1:
        score_ali += 1
        print(f"Le score de Ali est : {score_ali}")
        
    elif ali == "f" and ordi == 2:
        egalite += 1
        print("egalite")  
        
    elif ali == "f" and ordi == 3:
        score_ordi += 1
        print(f"Le score de l'ordi est : {score_ordi}")
        
    elif ali == "c" and ordi == 1:
        score_ordi += 1
        print(f"Le score de l'ordi est : {score_ordi}")
        
    elif ali == "c" and ordi == 2:
        score_ali += 1
        print(f"Le score de Ali est : {score_ali}")
        
    elif ali == "c" and ordi == 3:
        egalite += 1
        print("egalite")    
        
    else:
        print("Utiliser (p) (f) (c)")
        
        
        
        

   
    