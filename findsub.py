mstr=input("Eter a String: ")
substr=input("Enter the substring: ")
n=mstr.find(substr,0,len(mstr))
if n==-1:
    print('Sub not found')
else:
    print('Found at index: ',n) #index number will be the first character
    #of substring
try:
    m=mstr.index(substr,0,len(mstr))
except ValueError:
    print('Not Found')
else:
    print('Found at index: ',m)
    
