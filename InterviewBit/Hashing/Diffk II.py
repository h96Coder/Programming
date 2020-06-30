class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(list(set(A)))==len(A) and B==0:
            return 0
        if len(A)<=1:
            return 0
        d={}
        for i in range(len(A)):
            d[A[i]+B]=0
            d[A[i]-B]=0
        for i in range(len(A)):
            if A[i] in d:
                return 1
        return 0
            
                
                
                
            
