
A= [10,0,19,2,85,66]
for i in range(len(A)): 
    # Find the minimum element in remaining  
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j         
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
print(A)