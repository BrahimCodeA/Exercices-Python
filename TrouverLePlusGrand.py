def PositionEltListe(L,x):
    x_indices = []
    
    for i in range(len(L)):
        if L[i] == x:
            x_indices.append(i)
            
    if len(x_indices) == 0:
        print(f"L'element {x} n'est pas dans la liste {L}")
    return x_indices
        
         
print(PositionEltListe([1,2,3,6,8,7,3],3))