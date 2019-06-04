import math
def linear_search(item, arr):
    stuff = ''
    for i in arr:
        if i == item:
            stuff = item
        else:
            stuff = 'not found'
    return stuff


def bin_search(item, arr):
    left = len(arr) - 1
    right =  0
    mid = (left + right)/2
    while arr[math.floor(mid)] > item :
        mid = (left + right)/2
        if item < arr[mid]:
            left = mid + 1
        if item > arr[mid]:
            right = mid -1
        if item == mid:
            print (arr[mid])
            pass
        print(int(mid))
    return  arr[mid]

        
arr = [3,4,6,8,9,10,12,13,15, 19, 21]
item =  9
print(bin_search(item, arr))