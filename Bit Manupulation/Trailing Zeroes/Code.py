class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        cnt=0
        for i in range(32):
            if(A & (2<<i)==0):
                cnt+=1
            else:
                break
        return cnt
