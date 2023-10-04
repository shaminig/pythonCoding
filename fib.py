end_value=int(input("enter the number"))
f=0
s=1
for i in range(0,end_value):
    if i <= 1:
        result = i
    else:
        result=f+s
        f=s
        s=result
    print(result)