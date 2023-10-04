print("Welcome to the Love calculator")
name1=input("Enter the first name  ")
name2=input("enter the second name  ")
lc_name1=name1.lower()
lc_name2=name2.lower()
combine_name=lc_name1+lc_name2
print(combine_name)
true_count=combine_name.count('t')+combine_name.count('r')+combine_name.count('u')+combine_name.count('e')
love_count=combine_name.count('l')+combine_name.count('o')+combine_name.count('v')+combine_name.count('e')
love_score=str(true_count)+str(love_count)
actual_score=int(love_score)
print(actual_score)
if(actual_score<10):
    print("you are like mentos and coke")
else:
    print(f"you are great,your score is {actual_score}")