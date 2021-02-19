#Write a Python program to accept a filename from the user and print the extension of that.
file_namee= input("Ener a file name: ")
file_split=file_name.split('.')
print("Extension is: ",repr(file_split[-1]))
