class Solution:
    def passThePillow(self, n: int, t: int) -> int:
    #The first set of solution
        # x=2*(n-1)
        # t %=x
        # return t+1 if (t<n) else (x-t+1)

    #The Second set of solution
        # x=2*(n-1)
        # t %=x
        # temp =abs(t-(n-1))
        # return n-temp
    #Thirs set of solution which is with much less space complexity
        # return n - abs(n - 1 - t % (n * 2 - 2));