def multipleOfTwo(n):
    i = n
    if i == 1:
        return i
    while i > 1:
        i = i/2
    if i == 1.0:
        return True
    else:
        return False

        

def toStream(arr):
    myList = []
    for n in range(len(arr)):
        remainder = 0
        if multipleOfTwo(arr[n]) == False:
            counter = 0
            while multipleOfTwo(arr[n]) == False:
                arr[n] -= 1
                counter += 1
            remainder = counter
            try:
                arr[n+1] += remainder
            except IndexError:
                remainder = 0
        myList.append(arr[n])
    print(max(myList))


# print(multipleOfTwo(31))
toStream([1000, 7, 3, 9,6,5,4,2,32,11,1000,1000,1,2,2,22,2,2,21,12,21,21,22])