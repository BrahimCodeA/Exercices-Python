def union_ensembles(ensemble1, ensemble2):
    union = set(ensemble1)
    for elt in ensemble2:
        union.add(elt)
        
    return union

# Test de la fonction
print(union_ensembles({1, 2, 3}, {3, 4, 5}))
