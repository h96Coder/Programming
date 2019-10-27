'''
Maximum Value Contiguous subsequence
'''
def mvcs(A):
    B=[0]*len(A)
    if A[0]>0 :
        B[0]=A[0]
    else:
        B[0]=0
    for i in range(1,len(A)):
        if(B[i-1]+A[i]>0):
            B[i]=B[i-1] + A[i]
        else :
            B[i]=0
    return B
def max_mvcs(B):
    maxi=0;
    for i in range(0,len(B)):
        if(B[i]>maxi):
            maxi=B[i]
    return maxi
if __name__ == '__main__':
   # A =[-2,11,-4,13,-5,2]
    A= [1,-3,4,-2,-1,6]
    B = mvcs(A)
    print("Max sum continous subsequence: ", max_mvcs(B))
