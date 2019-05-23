class Node(object):
    def __init__(self, val, nextNode=None):
        self.val = val
        self.nextNode = nextNode
    
    def get_val(self):
        return self.val
    
    def get_next(self):
        return self.nextNode
    
    def set_next(self, new_next):
        # resets the pointer to a new node
        self.nextNode = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


    def insert(self, new_val):
        new_node = Node(new_val) #initialize new node along with empty memory allocation
        new_node.set_next(self.head)    #push old head aside by pointing newnode next as it's head
        self.head = new_node


    def count(self):
        current  = self.head
        count = 0
        while current :# while my current is not null
            count +=1
            current = current.get_next() #move foreward
        return count

    def search(self, search_val):
        current = self.head
        found = False
        try:
            while current and found is False:
                if current.get_val() == search_val:
                    found = True
                current = current.get_next()
        except ValueError:
            return 'Value not found'
        return current # because current the loop stopped at the found value



    def delete(self, delete_val):
        # begin at the top of the list where there parameters are satisfied
        current = self.head
        found = False
        previous = None

        while current and found is False:
            if current.get_val() == delete_val:
                # we found the delete value
                found = True
            else:
                # move foreward
                previous = current
                current = current.get_next()
            if current is None:
                # current is not found because it is only none at the end of a list
                raise ValueError('Value not found')
        if previous is None:
            # it means we are still at the head
            self.head = current.get_next()
        # if delete is successful, break current link by overlooking current
        previous.set_next(current.get_next())




def count():
    myList = ['boy', 'girl', None, 'different', 'sexes']
    i = 0
    while myList[i]:
        print(myList[i])
        i+=1
count()