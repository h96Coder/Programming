class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        d={}
        for i in range(len(A)-1,-1,-1):
            d[B-A[i]]=i
        #print(d)    
        p=-1
        q=-1
        mi=1000000007
        mi1=1000000007
        for i in range(len(A)):
            if A[i] in d:
                x=i
                y=d[A[i]]
                #print(x,y)
                if x>y:
                    x,y=y,x
                elif x==y:
                    continue
                if mi>y:
                    mi=y
                    p=x
                    q=y
                elif mi==y:
                    if mi1>x:
                        p=x
        return [p+1,q+1]
                
