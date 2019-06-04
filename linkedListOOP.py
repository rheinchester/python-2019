class linkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def gethead(self):
        return self.head

    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.next is None:
                currentNode.next = node
                break
            currentNode = currentNode.next

    def delete(self, head, valueToDelete):
       previousNode = None
       head = self.head
       currentNode = head

       if valueToDelete == currentNode:
           tempVal = currentNode.next
           currentNode = currentNode.next 
            
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value,"->")
            currentNode = currentNode.next
        print("None")

l1  = linkedList()

print(l1.gethead(), '---')
l1.insert('3')
l1.printLinkedList()
l1.insert('6')
# l1.printLinkedList()
l1.insert('9')
# l1.printLinkedList()
# l1.delete('3','3')
l1.printLinkedList()
print(l1.gethead().value, '---')

