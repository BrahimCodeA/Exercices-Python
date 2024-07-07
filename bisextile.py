# Demander au user l'anné
annee = int(input("Entrez l'année : "))
if ( (annee % 4 == 0) and (annee % 100 != 0) or (annee % 400 == 0) ):
    print(f"L'année {annee} est bissextile") 
else:
    print(f"L'anné {annee} n'est pas bissextile")

