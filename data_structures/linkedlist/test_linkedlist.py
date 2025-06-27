# Ensure import works
from linkedlist import LinkedList, Node

# This should return an instance of a LinkedList class
llist = LinkedList()
print(llist)

# Test number
test_num = 1

# * Assertion methods
def debugTest():
    # Define test_num as a global variable
    global test_num

    # todo: I can remove this later? Maybe we will only want to see something if it fails
    print(f"Test {test_num} passed")

    # Increment so that we can tell which test failed
    test_num += 1
    
def assertPresence(instance, attr):
    debugTest()
    if not hasattr(instance, attr):
        raise AttributeError(f"The attribute {attr} is not currently in the LinkedList class")
    
    
def assertVal(correct, actual):
    debugTest()
    assert correct is actual, f"The current value is {actual} but should be {correct}"

def assertType(correct, actual):
    debugTest()
    correct = type(correct)
    actual = type(actual)
    assert correct == actual, f"The current type is {actual} but should be {correct}"
    

            
    

# * Presence and initial values of the attributes when initializing an empty LinkedList
# .head
attrs = ['head', 'tail', 'size']
values = [None, None, 0]

for attr, value in zip(attrs, values):
    assertPresence(instance=llist, attr=attr)
    assertVal(correct=None, actual=llist.head)



# * Test .add()

llist.add(1)

# Check the presence and value of each attribute
# .head
values = [Node(1), Node(1), 1]

instance_attrs = llist.__dict__

for attr, value in zip(attrs, values):
    # Ensure that the instance contains the attribute
    assertPresence(instance=llist, attr=attr)
    
    # Get the appropriate attribute
    instance_attr = instance_attrs[attr]
    
    # Ensure that the attribute is of the appropriate type
    assertType(correct=value, actual=instance_attr)
    
    # Different attributes require different checks
    if attr in ['head', 'tail']:
        # Check to make sure that the data contained in each node is correct
        assertVal(correct=value.data, actual=instance_attr.data)
        
        # The head and tail node should be the same thing
        assertVal(correct=llist.head, actual=instance_attr)
        
        # The head and tail node should be the same thing
        assertVal(correct=llist.tail, actual=instance_attr)
    else:
        assertVal(correct=value, actual=instance_attr)





# * TBD

# correct_values = {
#     'type': type(LinkedList()),
#     'head': None,
#     'tail': None,
#     'size': 0
# }

# def node_as_dict(data, prev=None, next=None):
#     return {
#         'type': type(Node()),
#         'data': data,
#         'prev': prev,
#         'next': next

    
# def getAttrVal(instance, attr):
#     # Obtain the key value pairs for the class attributes
#     instance_attrs = instance.__dict__

#     # Get the current value of the attribute
#     return instance_attrs[attr]

# def assertAttrVal(instance, attr, value):
#     # Access the actual value of the attribute in the current instance
#     actual_value = getAttrVal(instance, attr)
    
#     # Access and compare the value of the current attribute
#     assertVal(value, actual_value)

#     # Increment and deub test number
#     debugTest()

# def assertAttr(instance, attr):
#     if not hasattr(instance, attr):
#         raise AttributeError(f"The attribute {attr} is not currently in the LinkedList class")
    
#     # Increment and deub test number
#     debugTest()
    
# def test(instance, attrs):
#     global correct_values
    
#     for attr in attrs:
#         # Check for presence
#         if not hasattr(instance, attr):
#             raise AttributeError(f"The attribute {attr} is not currently in the LinkedList class")
        
#         instance_attrs = instance.__dict__
        
#         # Check that the attribute type is correct
#         assertType(correct_values["type"], instance_attrs[attr])
        
#         assertVal(correct_values[attr], instance_attrs)