import random
uc=int(input("enter the number  "))
cc=random.randint(0,2)
print(cc)
if(uc==cc):
    print("draw")
elif uc==2 and cc==0:
    print("computer wins")
elif uc==0 and cc==2:
    print("you win")
elif(uc<cc):
    print("computer wins")
elif(uc>cc):
    print("you win")
else:
    print("game started")
