n=int(input())
x=1
for i in range(1,n+1):
    if(i==1 or i==n):
        print(" "*(n-i)+"*"*(2*i-1))
    else:
        print(" "*(n-i) + "*"+ " "*x + "*")
        x+=2
