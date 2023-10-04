str=input("enter the string")
print(str[2:3:-1])
rev_str=str[::-1]
print(rev_str)
if(str==rev_str):
    print("the string is palindrome")
else:
    print("not palindrome")
#method2
str_rev=""
for i in str:
    str_rev=i+str_rev
print(str_rev)