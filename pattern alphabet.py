# n=int(input())
# for i in range (1, n+1):
#     for i in range(1,i+1):
#         a=chr((i%26)+96)
#         if (i%26==0):
#             print("z",end="")
#         else:
#             print(a,end="")
#     print()
# #The alphabet will be printed in "n" number of lines where each line will be updated with the alphabets.
# #After z "a" will be repeated

# # n=int(input())
# # j=n
# # for i in range (1,n+1,2):
# #     for x in range(1,j+1):
# #         print(" "*j,end="")
# #         j=j-1
# #         break
# #     for k in range (1,i+1):
# #         print("*"*i,end="")
# #         break
# #     print()
# # # Pyramid patter of *

# n=int(input())
# x=1
# for i in range (1, n+1):
#     for j in range(i):
#         print(x, end=" ")
#         x=x+1
#     x=x-1