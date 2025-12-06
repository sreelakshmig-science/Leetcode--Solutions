# Counting the number of duplicate elments
li=[1,2,1,1,2,2,3,3,4,5]
count=0
for i in li[:]:
    if (li.count(i)>1):
        count+=1
        for j in range(li.count(i)):
            li.remove(i)
        print(li)
print(count)

#move zeroes to the last leetcode-283
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        for j in range(len(nums)):
            if (nums[j]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            