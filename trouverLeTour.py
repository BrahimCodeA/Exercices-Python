nbr = 0
user_nbr = int(input("Entrez votre nombre : "))

while user_nbr != 0:
    nbr += 1
    user_nbr //= 10

print(f"Le nombre a {nbr} chiffres.")
