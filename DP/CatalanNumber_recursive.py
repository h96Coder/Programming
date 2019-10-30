'''
   Catalan Number - Number of BST of n nodes
   
'''
   
def CatalanNumber_recursive(n):
    if n==0:
        return 1
    sum =0
    for i in range(1,n+1):
        sum = sum + CatalanNumber(i-1) * CatalanNumber(n-i)
    return sum
if __name__=="__main__":
    print(CatalanNumber(2))
