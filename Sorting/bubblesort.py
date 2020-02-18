def bubblesort(A):
    k=len(A)
    for j in range(k,-1,-1):
        for i in range(0,j-1):
            if(A[i]>A[i+1]):
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
        k=k-1
    return A
A=[5,4,10,2,11]
print(bubblesort(A))
