n=int(input("enter the number"))
temp=n
s=0
length=len(str(n))
print(length)
while n>0:
    r=n%10
    s=s+r**length
    n=n//10

if(temp==s):
    print("it is armstron num")
else:
    print("not armstrong")