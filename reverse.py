n=int(input("enter a number:"))
s=0
while(n):
    a=n%10
    s=s*10+a
    n=n//10
print(s)
