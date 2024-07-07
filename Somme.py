n = int(input("Entrez un nombre : "))
s = 0
j = 1
for i in range(n):
    s = s + (j ** 2)
    j = j + 2
print(s)