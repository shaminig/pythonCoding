array=[100,12,5,89,20,]
print("the original array",array)
# print(array[0],array[1],array[2])(fetch elements of array using index)
n=len(array)
print(n)
for i in range(n):
    for j in range(i+1,n):
        if array[i]>array[j]:
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
print("the sorted array in ascending order",array)



