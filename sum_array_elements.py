#To find sum of array elements
array2=[1,2,3,4,5]
sum=0
for i in range(5):
    sum+=array2[i]
print(sum)

#To add elements in odd positions
sum=0
for i in range(0, 5, 2):
    print("Elements in odd position",array2[i])
for j in range(0, len(array2), 2):
    sum+=array2[j]
print("sum of elements in odd position",sum)
# print(array2[::2]) (using slicing)

