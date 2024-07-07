# Demander au user un caractére
caractére = input("Entrez un caractére : ")
if ( ("A" <= caractére and "Z" >= caractére) or ("a" <= caractére and "z" >= caractére) ):
    print(caractére, "est un alphabet")
elif ("0" <= caractére and caractére <= "9"):
    print(caractére, "est un nombre")
else:
    print(caractére, "est un caractére speciale")