class Solution:
    def countPermutations(self, A):
        ans = 1; M = 10**9+7
        for i in range(1, len(A)):
            c = sum(A[j] < A[i] for j in range(i))
            if c == 0: return 0
            ans = ans * c % M
        return ans
