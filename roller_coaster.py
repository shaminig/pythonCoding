height=int(input("enter the height"))
if(height>120):
    print("you can ride")
    bill=0
    age=int(input("enter your age"))
    if(age<12):
        bill=5
        print("your ticket is 5$")
    elif(age>18):
        bill=7
        print("your ticket is 7$")
    else:
        if(12<=age>=18):
            bill=10
            print("you ticket is 10$")
    photo=input("want to take photo")
    if(photo=='y'):
        bill+=3
        print(f"your bill is {bill}")
else:
     print("you cant ride")







