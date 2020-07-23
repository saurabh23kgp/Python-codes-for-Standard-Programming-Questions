class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        num=0
        for i in range(32):
            if (A & 1<<i):
                num+=1
        return  num
