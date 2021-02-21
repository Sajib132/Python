#Python program to search a string in a given group of strings.
str=[x for x in input("Enter some string: ").split(',')]
print("You have entered: ",str)
v=input("Enter what you are searching for?")
flag=False
for i in range(len(str)):
    if v==str[i]:
        print('FOund at index: ',i)
        flag=True
if flag==False:
    print('Not Found')
