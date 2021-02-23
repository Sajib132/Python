#python program using map() function
def sqr(lst):
    return lst*lst
    
lst=[1,2,3,4]
lst1=list(map(sqr,lst))
print(lst1)

# a lambda function 
lst=[98,77,43,90]
lst1=list(map(lambda x: x*x,lst))
print(lst1)
