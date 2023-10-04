# #left rotation
# array=[1,2,3,4,5]
# shift=3
# n=len(array)
# for j in range(0,shift):
#     first=array[0]
#     for i in range(0,n-1):
#         array[i]=array[i+1]
#     array[n-1]=first
# print(array)

#Right Rotation
#reversal algo. for rotation of arrays
array=[1,2,3,4,5]
shift=3
n=len(array)
for j in range(0,shift):
    last=array[n-1]
    for i in range(n-1,-1,-1):
        array[i]=array[i-1]
    array[0]=last
print(array)


