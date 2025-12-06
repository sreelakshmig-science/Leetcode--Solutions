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
#reverse a list without build-in function
li=[1,2,3,4,5]
for i in range(len(li)//2):
    li[i], li[len(li)-i-1]=li[len(li)-i-1],li[i]
start=0
end=len(li)-1
while (start<end):
    li[start],li[end]=li[end],li[start]
    start+=1
    end-=1
print(li)
print(li[::-1])

#Diagonal difference
# li=[[1,2,3],[3,5,7],[9,10,11]]
# d1=d2=0
# for i in range(len(li)):
#     for j in range(len(li[0])):
#         if(i==j):
#             d1+=li[i][j]
#         if(i+j==len(li)-1):
#             d2+=li[i][j]
# print(abs(d1-d2))

#Rotate 90
#li=[[1,2,3],[3,5,7],[9,10,11]]
# for j in range(len(li[0])):
#     for i in range(len(li)-1,-1,-1):
#         print(li[i][j],end=' ')
#     print()