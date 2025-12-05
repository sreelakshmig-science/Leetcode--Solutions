class Solution:
    def numWaterBottles(self, nB: int, nE: int) -> int:
        ans=nB
        while (nB>=nE):
            x=nB//nE
            ans+=x
            nB= x+(nB%nE)
        return ans

        