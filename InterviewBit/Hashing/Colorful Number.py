class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A=str(A)
        if '0' in A and len(A)>1:
            return 0
        B=[1]
        d=set()
        for i in range(1,len(A)+1):
            B.append(B[i-1]*int(A[i-1]))
        #print(B)
        for i in range(1,len(A)+1):
            for j in range(i,len(B),i):
                x = int(B[j]/B[j-i])
                if x in d:
                    return 0
                else:
                    d.add(x)
                #print(d)
        return 1
                
                
                 
                
                
                
