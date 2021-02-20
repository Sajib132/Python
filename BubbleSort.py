#A python program to sort the array elements using bubble sort tecnique
from array import *
el=[int(x) for x in input("Enter the elements: ").split(",")]
print("Entered values are: " ,el)

n=len(el)
p=n-1
flag=False
for i in range(p):
    for j in range(p-i):
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
