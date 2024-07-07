n = int(input("Entrez un nombre : "))
s = 0

for i in range(1,n):
    if n % i == 0:
        s = s + i
if n == s:
    print(f"{s} est un nombre parfait")
else:
    print(f"{s} n'est pas un nombre parfait")