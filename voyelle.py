user = input("Entrez un mot : ")
voyelle = ["a","e","i","o","u"]
nbr_voylle = 0
nbr_consonne = 0

for lettre in user:
    if lettre in voyelle:
        nbr_voylle += 1
    else:
        nbr_consonne += 1
print(f"Nombre de voyelle : {nbr_voylle}")
print(f"Nombre de consonnes : {nbr_consonne}")