class Solution:
    # @param A : integer(total chords)
    # @return an integer
    def chordCnt(self, A):
        n=2*A
        ways=[0 for _ in range(n+1)]
        ways[0]=1
        ways[2]=1
        for i in range(4,n+1,2):
            for j in range(0,i-1,2):
                ways[i]+=ways[j]*ways[i-2-j]
        return (ways[n])
