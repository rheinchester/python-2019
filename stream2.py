def multipleOfTwo(n):  #log(n)
    i = n
    counter = 0
    newList = []
    if i == 1:
        return i
    while i > 1:
        i = i/2
        counter+=1
        # print()
        newList.append(i)
    if i == 1.0:
        # print(counter)
        return newList
    # print(counter)
    return False

        

def toStream(arr):
    myList = []
    multipleNum = 0
    for n in range(len(arr)):
        if multipleOfTwo(arr[n]) is not False:
            multipleList = multipleOfTwo(n)
            multipleNum = max(multipleList)
        if multipleOfTwo(arr[n]) == False:
            try:
                arr[n] = multipleNum
            except IndexError:
                pass
        myList.append(arr[n])
    print(myList)

# log2(n) + n**2
# print(max(multipleOfTwo(1024)))
toStream([1000, 7, 3, 9,6,5,4,2,32,11,1000,1000,1,2,2,22,2,2,21,12,21,21,22, 10000])
# multipleList = multipleOfTwo(2**199)
# print(multipleList)
