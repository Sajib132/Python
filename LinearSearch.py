#Python Code for Linear search
el=[int(x) for x in input("Enter the elements: ").split(",")]
print("Entered values are: " ,el)

find=int(input("Enter what you want: "))
#Linear Search Technique
flag=False
for i in range(len(el)):
    if find==el[i]:
        print("Found at index =",i)
        flag=True
if flag==False:
    print("Not Found")
