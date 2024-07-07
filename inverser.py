n = int(input("Entrez un nombre : "))
inverser = 0
while n != 0:
    inverser = (inverser * 10) + (n % 10)
    n = n // 10
print(f"L'inverse est {inverser}")