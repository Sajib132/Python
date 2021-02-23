#python program using filter() to filter out even numbers from a list
def is_even(lst):
    if lst%2==0:
        return True
    else:
        return False
lst=[12,13,14,6,17]
lst1=list(filter(is_even,lst))
print(lst1)
# a lambda function that returns even number from a list
lst=[98,77,43,90]
lst1=list(filter(lambda x: (x%2==0),lst))
print(lst1)
