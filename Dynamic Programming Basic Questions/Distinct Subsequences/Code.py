class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        m=len(A)
        n=len(B)
        if(n>m):
            return 0
        ways=[[0 for _ in range(n+1)] for __ in range(m+1)]
        for rows in ways:
            print(rows)
        
        for i in range(1,n+1):
            ways[i][0]=0
      
        for i in range(m+1):
            ways[0][i]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(B[i-1]!=A[j-1]):
                    ways[i][j]=ways[i][j-1]
                else:
                    ways[i][j]=ways[i][j-1]+ways[i-1][j-1]
        return ways[n][m]
