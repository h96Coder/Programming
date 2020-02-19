def insertionsort(A):
    for i in range(1,len(A)):
        p=i
        while A[p-1]>A[p]:
                A[p],A[p-1]=A[p-1],A[p]
                p=p-1
                if p-1<0:
                    break
A=[3,2,1]
insertionsort(A)
print(A)
