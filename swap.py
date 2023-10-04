# n1=int(input("entr the 1stnum"))
# n2=int(input("enter the 2nd num"))
# n3=n1
# n1=n2
# n2=n3
# print("n1=",n1)
# print("n2=",n2)

# without temporary variable #1
a1=int(input("enter the 1st num"))
a2=int(input("enter the 2nd num"))
# a1,a2=a2,a1  method#1
a1=a1+a2    #method2
a2=a1-a2
a1=a1-a2
print("the value of a1 and a2 are:",a1,a2)

