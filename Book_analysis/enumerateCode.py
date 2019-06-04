
#Enumerate helps u to keep count of pur iterators
def enumerate_demo():
    list_item = ['eat', 'sleep', 'bathe', 'deep']
    print(list(enumerate(list_item)))
    # prints --> [(0, 'eat'), (1, 'sleep'), (2, 'bathe'), (3, 'deep')]

    # Using Enumerate object in loops

    # Python program to illustrate 
    # enumerate function in loops 
    l1 = ["eat","sleep","repeat"] 
    
    # printing the tuples in object directly 
    for ele in enumerate(l1): 
        print (ele )
    print 
    # changing index and printing separately 
    for count,ele in enumerate(l1,100): 
        print (count,ele )
