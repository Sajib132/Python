#Write a program to generate python program
num=int(input("How man Fibonaci you want? "))
f1=0
f2=1
count=2
if num==1:
    print(f1)
elif num==2:
    print(f1, '\n', f2, sep='')
else:
    print(f1,'\n', f2, sep='')
    while count<num:
        f=f1+f2
        print(f)
        f1,f2=f2,f
        count+=1
