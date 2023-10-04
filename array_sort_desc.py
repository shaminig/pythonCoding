array1=[1,8,345,12,98,0,67]
print("the original array")
print(array1)
n=len(array1)
print("the length of the array",n)
for i in range(n):
    for j in range(i+1,n):
        if array1[i]<array1[j]:
            temp=array1[i]
            array1[i]=array1[j]
            array1[j]=temp
print("the sorted array in descending order")
print(array1)
print("the largest element is",array1[0])

#To find the second largest number in an array
print("second largest element is")
print(array1[1])