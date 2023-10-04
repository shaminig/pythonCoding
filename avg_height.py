num_heights=int(input("enter the no of heights of the students"))
l=[]
for i in range(num_heights):
    heights=int(input("enter the heights"))
    l.append(heights)
print(l)
add = 0
for j in l:
    add = add+j
print(add)
average=(add/num_heights)
print(round(average))