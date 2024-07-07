# Écrire dans un fichier
with open("mon_fichier.txt", "w") as f:
    f.write("Bonjour, monde !")

# Lire depuis un fichier
with open("mon_fichier.txt", "r") as f:
    contenu = f.read()
    print(contenu)
