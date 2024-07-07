a = int(input("Entrez un nombre : "))
b = int(input("Entrez un deuxiéme nombre : "))


if a > b:
    min = b
else:
    min = a
for i in range(1, min+1):
    if a % i == 0 and b % i == 0:
        pgcd = i
        
print(pgcd)
        