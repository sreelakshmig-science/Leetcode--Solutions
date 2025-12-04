class Solution:
    def canWinNim(self, n: int) -> bool:
        if(n%4==0): #the logic of the question is the condition should return False when 'n' is a multiple of 4
            return False
        else:
            return True
#The same if else logic can be implemented in a single return statement. Here the space complexity is lower.
          #return(n%4!=0) 
