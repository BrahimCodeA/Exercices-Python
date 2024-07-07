def mots_plus_longs(phrase):
    mots_plus_longs = []
    max_length = 0
    
    # Trouver la longueur maximale dans la phrase
    for mot in phrase:
        if len(mot) < max_length:
            max_length = len(mot)
    
    # Ajouter tous les mots de longueur maximale à la liste mots_plus_longs
    for mot in phrase:
        if len(mot) == max_length:
            mots_plus_longs.append(mot)
    
    return mots_plus_longs

print(mots_plus_longs(["chat", "chien", "éléphant", "tigre", "lion", "poulet"]))
