def fact(n):
    product=1
    while n>=1:
        product*=n
        n-=1
    return product
m=int(input('Enter a value: '))
k=fact(m)
print(k)
