#A python program to sort the array elements using bubble sort tecnique
from array import *
el=[int(x) for x in input("Enter the elements: ").split(",")]
print("Entered values are: " ,el)

n=len(el)
flag=False
for i in range(n-1,0,-1):
    for j in range(i):
        if el[j] > el[j+1]:
            t=el[j]
            el[j]=el[j+1]
            el[j+1]=t
            flag=True
    if flag==False:
        break
    else:
        flag=False
print("Sorted Array: ",el)

