def printLcs(s,s1,mat):
    result = ""
    sizes = len(s)
    sizes1 = len(s1)
    for i,j in zip(range(sizes,0,-1),range(sizes1,0,-1)):
        print (mat[i][j])
    j=sizes1
    i=sizes
    while(i>0 and j>0):
            if(s[i-1]==s1[j-1]):
                result = result + s[i-1]
                i= i-1
                j = j-1
            elif(mat[i][j-1]>mat[i-1][j]):
                j = j-1
            else :
                i =i-1
    return result
def Lcs(s,s1):
    print("Elemets : ")
    sizes=len(s)
    sizes1 = len(s1)
    mat = [[0 for j in range(0,sizes1+1)]for i in range(0,sizes+1)]
    for i in range(1,sizes+1):
        es = s[i-1]
        for j in range(1,sizes1+1):
            es1 = s1[j-1]
            if( es == es1):
                mat[i][j]=mat[i-1][j-1]+1
            else:
                mat[i][j] = max (mat[i-1][j],mat[i][j-1])
    return mat
if __name__=="__main__":
    s ="acbaed"
    s1 ="abcadf"
    mat = Lcs(s,s1)
    for i in range(0,len(s)+1):
        print(end="\n")
        for j in range (0,len(s1)+1):
            print (mat[i][j],end =" ")
    result = printLcs(s,s1,mat)
    print (result)
