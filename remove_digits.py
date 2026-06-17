n=int(input("Enter a value:"))
r=int(input("Enter a number to remove digit:"))
b=1
s=0
while(n):
    a=n%10
    if(a!=r):
        s=s+a*b
        b=b*10
    n=n//10
print(s)
