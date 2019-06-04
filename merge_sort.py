def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        half = int(len(arr)/2)
        left = merge_sort(arr[:half])#recursively break left half to a single node
        right = merge_sort(arr[half:])#recursively break right half to a single node
        return merge(left, right) 
        # print(left)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1
    return result


arr = [5, 2, 4, 6, 1, 3, 9, 7, 8]
# half = int(len(arr)/2)
print(merge_sort(arr))
# print(arr[:half])
# convert to c# later
