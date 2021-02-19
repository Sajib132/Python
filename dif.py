#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
value = int(input("Enter a number: "))
dif = value -17
print("Difference is: ",dif)
if value>17:
    difr=abs(dif*2)
    print("double value :" ,difr)
