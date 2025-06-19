def binay_search(lst, target):
    first = 0
    last = len(lst) - 1

    while first <= last:
        midpoint = (first + last)//2
        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] > target:
            last = midpoint  - 1
        else:
            first = midpoint  + 1
    return None

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

print(binay_search(numbers, 1))