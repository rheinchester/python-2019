def bsort(arr):
    swapped = False
    while not swapped:
        swapped = True
        i = 0
        while i < len(arr)-1:
            if arr[i]> arr[i+1]:
                # switch
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                # report swapped as false
                swapped = False
            i+=1
        # if for all items, swapped is false, break out of loop
    return arr



arr = [3,1,2,4,9,8,7,1,6]
print(bsort(arr))