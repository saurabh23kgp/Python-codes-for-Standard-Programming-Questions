class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        n=len(A)
        LIS=[1 for _ in range(n)]
        for j in range(1,n):
            for i in range(0,i):
                if(A[j]>A[i] and LIS[i]+1>LIS[j]):
                    LIS[j]=LIS[i]+1
        
