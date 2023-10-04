
array=[189,345,67,34,74,1,8,16]
print("the original array is")
print(array)
n=len(array)
print("the length of the array",n)
largest=array[0]
for i in range(1,n):
    if largest<array[i]:
     largest=array[i]
print("the largest number in the array is",largest)




