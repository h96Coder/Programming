def partition(A,i,j):
    if i>=j:
        return;
    mid= int((i+j)/2)
    #print(mid)
    partition(A,i,mid)
    partition(A,mid+1,j)
    merge(A,i,mid,j)
def merge(A,i,mid,j):
    #print(i,mid,j)
    l=[]
    r=[]
    for p in range(i,mid+1):
        l.append(A[p])
    for p in range(mid+1,j+1):
        r.append(A[p])
    #print(l,"->",r,"->",mid)

    k,s,t=i,0,0
    while(True):
        #print(A)
        if(s>=len(l) or t>=len(r) ):
            break;
        if(l[s]<r[t]):
            A[k]=l[s]
            s=s+1
        else:
            A[k]=r[t]
            t=t+1
        k=k+1
    for x in range(s,len(l)):
        A[k]=l[x]
        x=x+1
        k=k+1
    for x in range(t,len(r)):
        A[k]=r[x]
        x=x+1
        k=k+1
A=[5,4,3,2,1,10,9]
partition(A,0,len(A)-1)
print(A)
