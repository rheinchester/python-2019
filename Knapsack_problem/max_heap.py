def max_heapify(A, i):
    """ where A is the heap , i is the node,s position """
    # ensure to  create copy of the list
    l = 2 * i
    r = (2 * i) + 1
    if l <= len(A) and A[l] > A[i]:#base case
        print(A[i])
        largest = l
    else:
        largest = i
    if r<=len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
    return largest

def build_max_heap(A):
    half = int(len(A)/2)
    for i in reversed(range(1, half+1)):
        # print(i) 
        max_heapify(A, i)
    return A
# Height of a binary tree is bounded by log n
heap_list =[4,1,3,2,16,9,10,14,8,7 ]

print(build_max_heap(heap_list))

# How to reverse a list
# reversed(range(len(A)))
