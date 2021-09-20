def selection_sort(vector):
    nb = len(vector)
    for actual in range(0,nb):    
        mas_pequeno = actual
        for j in range(actual+1,nb) :
            if vector[j] < vector[mas_pequeno] :
                mas_pequeno = j
        if min is not actual :
            temp = vector[actual]
            vector[actual] = vector[mas_pequeno]
            vector[mas_pequeno] = temp

arr = [9,8,1,2,6,4,5]
selection_sort(arr)
print(arr)
