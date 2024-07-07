def AjoutContact(contacts):
    nom = input("Entrez le nom contact : ")
    telephone = input("Entrez le numéro de téléphone du contact : ")
    
    contacts[nom] = {"téléphone": telephone}
    
    return contacts

def SupprimerContact(contacts):
    delete_contact = input("Quel contact supprimer ? ")
    if delete_contact in contacts:
        del contacts[delete_contact]
        print(f"Le contact '{delete_contact}' a été supprimé avec succès.")
    else:
        print(f"Le contact '{delete_contact}' n'existe pas dans la liste.")
        
def RechercheContact(contacts):
    recherche_contact = input("Quel contact recherchez-vous ? ")
    if recherche_contact in contacts:
        print(f"{recherche_contact} est bien dans vos contact")
        print(contacts[recherche_contact])
    else:
        print(f"{recherche_contact} n'est pas dans votre liste de contact")
        
def ModifierContact(contacts):
    modif_contact = input("Quel contact souhaitez-vous modifier ? ")
    if modif_contact in contacts:
        nouveau_nom = input("Entrez le nouveau nom du contact : ")
        nouveau_telephone = input("Entrez le nouveau numéro de téléphone du contact : ")
        nouveau_email = input("Entrez la nouvelle adresse email du contact : ")
        
        # Mise à jour des informations du contact
        contacts[modif_contact]["téléphone"] = nouveau_telephone
        contacts[modif_contact]["email"] = nouveau_email
        if nouveau_nom != modif_contact:
            contacts[nouveau_nom] = contacts.pop(modif_contact)
        
        print("Le contact a été modifié avec succès.")
    else:
        print("Il n'y a aucun contact de ce nom.")


# Test des fonctions avec un dictionnaire de contacts existantcontacts
contacts = {"": {"": ""}}
print("Contacts avant ajout :", contacts)

nouveaux_contacts = AjoutContact(contacts)
print("Contacts après ajout :", nouveaux_contacts)

SupprimerContact(nouveaux_contacts)
print("Contacts après suppression :", nouveaux_contacts)

RechercheContact(nouveaux_contacts)

ModifierContact(nouveaux_contacts)
