def quicksort(A,i,j):
    pivote=A[j]
    x=i
    for p in range(i,j+1):
        if(pivote>=A[p]):
            temp=A[x]
            A[x]=A[p]
            A[p]=temp
            x=x+1
    return x-1
def partition(A,i,j):
    if(i>=j):
        return
    pivot=quicksort(A,i,j)
    #print(A,pivot)
    partition(A,i,pivot-1)
    partition(A,pivot+1,j)

A=[1,2,6,6,5]
partition(A,0,len(A)-1)
print(A)
