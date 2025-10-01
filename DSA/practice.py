
def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
# print(linear_search(numbers, 6))

numbers = [1,2,3,4,5,6,7,8,9,10]
def binary_search(lst, key):
    if len(lst) == 0:
        return False
    midpoint = len(lst)//2
    if lst[midpoint] == key:
        return midpoint
    else:
        if lst[midpoint] < key:
            return binary_search(lst[midpoint + 1:], key)
        else:
            return binary_search(lst[:midpoint], key)
    
print(binary_search(numbers, 9))
