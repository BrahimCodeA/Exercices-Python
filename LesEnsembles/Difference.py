def difference_ensemble(ensemble1, ensemble2):
    difference_resultat = set()
    for elt in ensemble1:
        if elt not in ensemble2:
            difference_resultat.add(elt)
            
    return difference_resultat
    
    
print(difference_ensemble({1, 2, 3}, {3, 4, 5}))