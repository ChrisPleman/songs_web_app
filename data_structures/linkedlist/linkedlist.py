class Node():
    def __init__(self, _data):
        self.data = _data
        self.next = None
        self.prev = None

# todos:
    # ? Add doc strings to each of the methods
        # add()
        # addFirst()
        # addAll()
        # removeFirst()
        # removeLast()
        # remove()
        # addToEmptyList()
        # raiseIfWrongDtype()
        # raiseIfEmpty()
        # isEmpty()
        # isHeadNode()
        # isTailNode()
    # ? Stress test each method
        # * See the following file: unit_tests/test_linkedlist.py
        # add()
        # addFirst()
        # addAll()
        # removeFirst()
        # removeLast()
        # remove()
        # addToEmptyList()
        # raiseIfWrongDtype()
        # raiseIfEmpty()
        # isEmpty()
        # isHeadNode()
        # isTailNode()

class LinkedList():
    
    def __init__(self, data=None):
        # Give option to instantiate with a node in place
        if data:
            node = Node(data)
            self.head = node
            self.tail = node
            self.size = 1
            self.dtype = type(data)
        else:
            self.head = None
            self.tail = None
            self.size = 0
            self.dtype = None
        
    def add(self, element):
        
        # Since we will be referencing this multiple times, it's better to save as a local variable
        new_node = Node(element)
        
        # If list is empty, the new node is both the head and the tail
        if self.isEmpty():
            self.addToEmptyList(new_node)
            return self
        
        # Enforcing data types
        self.raiseIfWrongDtype(element)
    
        # We don't need to loop, we just need access to the last node
        prev_tail_node = self.tail
        self.tail = new_node
        new_node.prev = prev_tail_node
        prev_tail_node.next = new_node

        # node = self.head

        # while True:
        #     if node.next:
        #         node = node.next
        #         continue
            
        #     # Adding a new element to the end of the list
        #     node.next = new_node
        #     new_node.prev = node
        #     self.tail = new_node
        #     break
        
        return self
    
    def addFirst(self, element):
        
        new_node = Node(element)
        
        # Can chain operations
        if self.isEmpty():
            self.addToEmptyList(new_node)
            return self
        
        # Enforcing data types
        self.raiseIfWrongDtype(element)
        
        # No looping required
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1
        
        return self
    
    def addAll(self, collection):
        # Nice and simple now
        for element in collection:
            self.add(element)
        
        return self
    
    def removeFirst(self):
        
        # Handling removal on an empty list
        self.raiseIfEmpty()
        
        # If removing node would make the list empty, just set the head and tail to none
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            # Garbage collection should handle the removed node
            self.head = self.head.next
            self.head.prev = None
            
        self.size -= 1
        
        return self
    
    def removeLast(self):
        
        # Handling removal on an empty list
        self.raiseIfEmpty()
        
        # If removing node would make the list empty, just set the head and tail to none
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            # Garbage collection should handle the removed node
            self.tail = self.tail.prev
            self.tail.next = None
            
        self.size -= 1
        
        return self
        
    
    def remove(self, element):
        
        # Can't remove what's not there
        self.raiseIfEmpty()
        
        # Can't remove what's not there (this time because of datatype diffs)
        self.raiseIfWrongDtype(element)
        
        # Start at the head
        node = self.head
        
        while True:
            # If there isn't any data left to check then we raise a ValueError as it was not contained in this list
            if not node.data:
                raise ValueError("Element not found in list.")
            
            # Doing this operation to reduce nesting
            # If it's not the right element, then we can just move on to the next node
            if element != node.data:
                node = node.next
                continue
            
            if not self.isHeadNode(node) or not self.isTailNode(node):
                node.prev.next = node.next
                node.next.prev = node.prev
                return self
            # Since this already handles lists of size 1, then I don't have to worry about including an and condition for the node being both head and tail
            elif self.isHeadNode(node):
                # This already handles lists of size 1
                self.removeFirst()
                return self
            elif self.isTailNode(node):
                # This already handles lists of size 1
                self.removeLast()
                return self
        
        
    # * Utility functions
    def addToEmptyList(self, new_node):
        self.head = new_node
        self.tail = new_node
        self.dtype = type(new_node.data)
        self.size += 1
        
    def raiseIfWrongDtype(self, element):
        # Enforcing data types
        if type(element) != self.dtype:
            raise TypeError(f'Invalid data type. Please pass data of type {self.dtype}.')
        
    def raiseIfEmpty(self):
        # Removes the number of times I'd have to repeat the following when removing from an empty list
        if self.isEmpty():
            raise IndexError("There are no nodes in this LinkedList instance.")
        
    def isEmpty(self):
        # Makes this more human readable
        return self.size == 0
    
    def isHeadNode(self, node):
        # As long as we check that the list isn't empty, then this should be fine
        return node is self.head
    
    def isTailNode(self, node):
        return node is self.tail
