import math
n=int(input("enter a number:"))
n1=n*n
n2=int(str(n1)[::-1])
n3=int(math.sqrt(n2))
n4=int(str(n3)[::-1])
if(n==n4):
    print("Adam number")
else:
    print("Not an adam number")
