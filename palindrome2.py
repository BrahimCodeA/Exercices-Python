user = input("Entrez un mot : ")
user_reversed = user[::-1]
if user_reversed.upper() == user.upper():
    print(True)
else:
    print(False)

