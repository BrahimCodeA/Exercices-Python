n = int(input("Entrez un nombre : "))
inverser = 0
original = n  # Sauvegardez le nombre original pour la comparaison à la fin
while n != 0:
    inverser = (inverser * 10) + (n % 10)
    n = n // 10

if original == inverser:
    print("Le nombre est un palindrome :", original)
else:
    print("Le nombre n'est pas un palindrome :", original)


