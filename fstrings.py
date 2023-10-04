# name='shamini'
# age=32
# height=1.67
# print("My name is " +name ,"My age is "+str(age)) #using +
# print("My name is" ,name,"my height is" ,height)#using comma
# print(f"My name is {name},My age is {age},My height is {height}" )#using fstrings

#program to calculate how many years left to reach 90 years
My_age=int(input("enter your age"))
years_left=90-My_age
days_left=years_left*365
months_left=years_left*12
weeks_left=years_left*52
print(f"I have {days_left}days,{weeks_left}weeks and {months_left}months left to reach 90 years ")
