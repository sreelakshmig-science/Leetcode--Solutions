class Solution:
    def findDelayedArrivalTime(self, x: int, y: int) -> int:
        return (x+y)%24 #the 24 hour cycle repeats.
