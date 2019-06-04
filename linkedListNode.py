# create Node that contains a value and a next node, that has a default value as none
class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

node1 = linkedListNode("3")         
node2 = linkedListNode("7")         
node3 = linkedListNode("10")
node4 = linkedListNode("21")

# now we link nodes
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4


currentNode = node1
while True:
    #  if the next node is empty, we have reached the end of the list
    print(currentNode.value,'->',)
    if currentNode.nextNode == None: 
        print("None")
        break
    currentNode = currentNode.nextNode # make nextnode the current node