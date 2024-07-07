Marrakech = 1000000
Agadir = 500000
nbr_annee = 0

while Marrakech > Agadir:
    Marrakech += 50000
    Agadir *= 1.08
    nbr_annee += 1
print(f"Il faut {nbr_annee} année")
