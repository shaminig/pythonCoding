
    # Implement your solution here
A=[1,3,6,4,1,2]
n=len(A)
for i in range(0,n-1):
    if A[i]==A[i+1]:
        print(i)
    else:
        print("null")