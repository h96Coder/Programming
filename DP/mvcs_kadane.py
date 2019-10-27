'''
 Kadane's Algorithm for max sum contigous sub-array
'''
def mvcs_kadane(A):
    sum=0
    cur_sum =0
    for i in range(0,len(A)):
         cur_sum=cur_sum+A[i]
         if(cur_sum<0):
             cur_sum=0
         if(cur_sum>sum):
             sum = cur_sum
    return sum
             
if __name__=="__main__":
    A=[1,-3,4,-2,-1,6]
    print("Max value contiguous suarray",mvcs_kadane(A))
