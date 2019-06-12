# build node
# build edge
class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

    def __str__(self):
        return self.name
class Edge(object):
    """ Assumes that src and dest are nodes """
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() +" -> "+self.dest.getName()

class Digraph(object):
    """edges is a dict mapping each node to a list of
        its children"""
    def __init__(self, edge):
        self.edges = {}

    def addNode(self, node):
        if node in self.edge:
            raise ValueError('Duplicate Node')
        self.edges[node] = []
    
    def addEdge(self, edge):
        # get source
        # get dest
        # if node does not have source or destnation it is not in graph
        # else, add the node as a key in edge dict
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edge and dest not in self.edge):
            raise ValueError(' There is no node' )
        return self.edge[src].append(dest)#bind it to the class edge, using self
    
    # children, has node, get node
    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if name == n.getName():
                return n
        else:
            raise NameError(name)
    
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                    + dest.getName() + '\n'
        return result[:-1]  # omit final newline

