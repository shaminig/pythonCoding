n=int(input("enter the number"))
temp=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
if(temp==rev):
    print("num is palindrome")
else:
    print("num not palindrome")