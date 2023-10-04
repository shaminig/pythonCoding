n=[0,10,-2,30,15,0,9,12]
i=['tom','cat','dog']
g=[13,'ram',True,8.9]
print(n[0:4])
print(n[1:5])
print(n[0:])
print(n[:])
print(n[1:8:3])#(start value,length of list,step size),to access specific values in list
n.sort()
print(n)
n.reverse()
print(n)
print(min(n))
print(max(n))
n.append(13) #takes only 1 argument
print(n)
n.extend([11,22,33,77,99])#adding a list
print(n)
n.sort()
print(n)
#inserting values at specific index position
n.insert(6,21)
print(n)
#other ways to assign values at specific index position
n[8]=78
print(n)
#replacing specific values in their index position
n[2:7]=[1,2,3,4,5]
print(n)
#removing a particular value
n.remove(2)
print(n)
#pop() removes values that are in the last position
n.pop()
print(n)
n.pop()
print(n)
#to find the length of the list
k=len(n)
print(k)
#using count function
n.extend([22,22,33,44,1])
print(n)
print("count of 22",n.count(22))
print("index of 33",n.index(22))