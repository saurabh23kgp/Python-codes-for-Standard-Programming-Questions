class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        n=len(A)
        if n==1:
            return 1
        lis=[1 for _ in range (n)]
        lds=[1 for _ in range(n)]
        for j in range (1,n):
            for i in range(0,j):
                if(A[j]>A[i] and lis[j]<lis[i]+1):
                    lis[j]=lis[i]+1
        for j in range(n-2,-1,-1):
            for i in range(n-1,j,-1):
                if(A[j]>A[i] and lds[j]<lds[i]+1):
                    lds[j]=lds[i]+1
        maximum=lis[0]+lds[0]-1
        for i in range(1,n):
            maximum=max(maximum,lis[i]+lds[i]-1)
        
        return maximum       
        
