def interscetion_ensemble(ensemble1, ensemble2):
    interscet_ensemble = set()
    for elt in ensemble1:
        if elt in ensemble2:
            interscet_ensemble.add(elt)

    return interscet_ensemble


print(interscetion_ensemble({1,2,3,4,5,6}, {3, 4, 5}))
