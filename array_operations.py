#To get array elements from the user
# array = input("Enter space-separated elements: ").split()
# print(array)

#To declare array elements
array1=[34,77,1,93,90]

#To search an element in an array
print(array1[0])
print(array1[4])

#To insert an element in an array
array1.append(78)
print(array1)

#To insert an element at particular position
array1[3]=66
print(array1)

#To delete an element in an array
array1.pop()
print(array1)
array1.remove(77)
print(array1)