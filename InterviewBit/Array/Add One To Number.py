class Solution:
    # @param A : list of integers
    # @return a list of integers
    
    def plusOne(self, A):
        re=0
        A=A[::-1]
        temp = A[0]+1
        if temp==10:
            A[0]=0
            re=1
        else:
            A[0]=temp
            for i in range(len(A)-1,-1,-1):
                if A[i]==0:
                        A.pop(i)
                else:
                    break
            return A[::-1]
            
        for i in range(1,len(A)):
            tem=int((A[i]+re)%10)
            re=int((A[i]+re)/10)
            A[i]=tem
        if re>0:
            A.append(re)
        return A[::-1]
        for i in range(len(A)-1,-1,-1):
            if A[i]==0:
                    A.pop(i)
            else:
                break
        return A[::-1]
                    
                
