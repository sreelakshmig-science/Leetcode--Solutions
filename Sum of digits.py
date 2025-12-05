x=int(input())
n=x
count=0

while x!=0:
    count+=1
    x=x//10

sum1=0
sum2=0
if (count%2==0):
    print("Invalid")
else:
    a=count//2
    for i in range (a):
        sum1 = sum1+(n%10)
        n=n//10
    n=n//10
    for i in range(a):
        sum2 = sum2+ (n%10)
        n=n//10
if(sum1==sum2):
    print("Valid")
else:
    print("Invalid")