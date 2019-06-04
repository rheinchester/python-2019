class Node(object):
    def __init__(self, val, nextNode=None):
        self.val = val
        self.nextNode = nextNode

    def get_val(self):
        return self.val
    
    def get_next(self):
        return self.nextNode

    def set_next(self, new_next):
        self.nextNode = new_next

class = LinkedList(object): 
    #when initializing a new list, ensure that the head starts as none
    def __init__(self, head=None):
        self.head = head
    

    def insert(self, data):
        # initialize new node from data
        new_node = Node(data)
        # make the list's head(being null), its next link
        new_node.set_next(self.head)
        # make node the head
        self.head = new_node
    
    def size(self):
        # start with zero and at the head
        count = 0
        # remember that self.head is a node which has the property of get next
        current = self.head 
        while current:
            count+=1
            current = current.get_next()
        return count

    def search (self, search_val):
        # start with the head, where data isn't found
        current  = self.head
        found = False
        while current and found is not True:
            # if val in current is the data, then we found it
            if current.get_val() == search_val:
                found = True
            else:
                # move to the next node
                current = current.get_next()
        if current is None:
            # if current is none, 
            # it either means we have reached the of the list or the list is empty,
            raise ValueError('Value not in list')
        return current

    def delete(self, delete_val):
        # start with the begining of the list
        current = self.head
        previous = None
        found = False
        while current and found is not True:
            if current.get_val() == delete_val:
                found = True
            else:
                # move foreward
                previous = current
                current = current.get_next()
        if previous is None:
            # i really don't understand this code
            self.head = current.get_next()
        if current is None:
            raise ValueError('Item not available')
        else:
            # break the link
            previous.set_next(current.get_next())