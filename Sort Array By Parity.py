class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        a=[]
        b=[]
        for c in A:
            if c%2==0:
                a.append(c)
            else:
                b.append(c)
        return a+b
        
#This has O(N) time and space
#Better solution
class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
 
 
