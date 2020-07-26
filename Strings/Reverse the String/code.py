#concept

s="   qxkpvo  f   w vdg t wqxy ln mbqmtwwbaegx   mskgtlenfnipsl bddjk znhksoewu zwh bd fqecoskmo        "
List=s.split(' ')
print(List)

#output will be:-
#['', '', '', 'qxkpvo', '', 'f', '', '', 'w', 'vdg', 't', 'wqxy', 'ln', 'mbqmtwwbaegx', '', '', 'mskgtlenfnipsl', 'bddjk', 'znhksoewu', 'zwh', 'bd', 'fqecoskmo', '', '', '', '', '', '', '', '']
#Thing here is that in starting and end there are 3 and 8 white spaces respectively. So we got 3 and 8 '' respectively in the list. But, if we look in the middle, n spaces lead to n-1 ''.



#The question is Given a string A. Return the string A after reversing the string word by word.
#Its an interviewbit question.

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        List=A.split(' ')
        List=[x for x in List if x!='']
        n=len(List)
        for i in range(n//2):
            List[i],List[n-i-1]=List[n-i-1],List[i]
        
        return ' '.join(List)
            























