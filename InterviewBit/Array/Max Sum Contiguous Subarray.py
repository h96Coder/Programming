class Solution:
    def maxSubArray(self, A):
        su=0
        current=0
        for i in range(0,len(A)):
            current+=A[i]
            if su<current:
                su=current
            if current<0:
                current=0
        if su==0:
            mn=-10000
            for i in range(0,len(A)):
                if(A[i]>mn):
                    mn=A[i]
            su=mn    
            
        return su
