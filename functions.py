class calculator:
    num=100


    def __init__(self,a,b):
       self.num1=a
       self.num2=b
       print("im called automatically")


    def getdata(self):
         print("Iam inside a function")

    def addition(self):
        return self.num1+self.num2+calculator.num


obj=calculator(2,3)
print(obj.addition())