# first node is the head, and last is the tail
#we know when a linked list ends when a node doesnt point to anything else
#like a treasure hunt with clues along the way
class Node:
    """
    An objct for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data
    



class LinkedList:
    head = None 
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        # takes O(n) linear time
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        print(count)
    
    def add(self, data):
        # this would be a prepend
        # adds new node as a head, O(1)
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        # search for first node containing data that mathces key
        # returns node or None
        #O(n)
        current = self.head

        while current:
            if current.data ==key:
                return current
            else: 
                current = current.next_node
        
        return None

    
    def __repr__(self):
        """
            Return a string representation of the list
            takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
        
            current = current.next_node
        
        return '->'.join(nodes)

    def insert(self, data, index):
        """inserts new node containint data at index positon
            Insertion takes O(1) but finding thenode at the insetion point takes O(n)
            therefore lineal time
        """

        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev = current
            next_node = current.next_node
            
            prev.next_node = new
            new.next_node = next_node
    
    def remove(self, key):
        """
            finding the node and then changing the references
            O(n)
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current


N1 = Node(10)
N2 = Node(14)
N1.next_node = N2

print(N1)
print(N1.next_node)

l = LinkedList()
l.head = N1
l.size()
l.add(4)
l.size()
print(l)
print(l.search(4))
l.insert(9,2)
print(l)