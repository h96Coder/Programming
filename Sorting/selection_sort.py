def selection_sort(A):
    for i in range(len(A)):
        min = i
        for j in range(i,len(A)):
            if(A[j]<A[min]):
                min=j
        A[min],A[i]=A[i],A[min]
    return A

A=[5,4,21,2,1]
print(selection_sort(A))
