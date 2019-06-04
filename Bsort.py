def Bsort(arr):
    swapped = False
    while not swapped:#as long as sort is not exhaustive, run loop
        swapped = True
        i = 0
        while i < len(arr)-1:
            if arr[i]> arr[i+1]:#where swap is true there is a greater value
                swapped = False
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                print (swapped)
            i+=1
    return arr


arr = [3,1,2,4,9,8,7,1,6]
print(Bsort(arr))
