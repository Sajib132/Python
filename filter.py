#python program using filter() to filter out even numbers from a list
def is_even(lst):
    if lst%2==0:
        return True
    else:
        return False
lst=[12,13,14,6,17]
lst1=list(filter(is_even,lst))
print(lst1)
