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


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        # initialize new node from data
        new_node = Node(data)
        # make the list's head(being null), its next link
        new_node.set_next(self.head)
        # make node the head
        self.head = new_node