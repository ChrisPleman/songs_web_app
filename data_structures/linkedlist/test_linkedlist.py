# Ensure import works
from linkedlist import LinkedList, Node

# This should return an instance of a LinkedList class
llist = LinkedList()
print(llist)

# Test number
test_num = 1

# * Assertion methods
def assertAttrVal(instance, attr, value):
    # Obtain the key value pairs for the class attributes
    instance_attrs = instance.__dict__

    # Get the current value of the attribute
    actual_value = instance_attrs[attr]

    # Access and compare the value of the current attribute
    if value is None:
        assert actual_value is value, f"The current value of the {attr} attribute is {actual_value} but should be {value}"
    else:
        assert type(actual_value) == type(value), f"The current value of the {attr} attribute is {actual_value} but should be {value}"

def assertAttr(instance, attr, value):
    if not hasattr(instance, attr):
        raise AttributeError(f"The attribute {attr} is not currently in the LinkedList class")
    else:
        # Ensure the value is correct for given attribute
        assertAttrVal(instance, attr, value)

        # Define test_num as a global variable
        global test_num

        # todo: I can remove this later? Maybe we will only want to see something if it fails
        print(f"Test {test_num} passed")

        # Increment so that we can tell which test failed
        test_num += 1

# * Presence and initial values of the attributes when initializing an empty LinkedList
# .head
assertAttr(instance=llist, attr="head", value=None)

# .tail
assertAttr(instance=llist, attr="tail", value=None)

# .size
assertAttr(instance=llist, attr="size", value=0)


# * Test .add()

llist.add(1)

# Check the presence and value of each attribute
# .head
assertAttr(instance=llist, attr="head", value=Node(1))
# .head.data

# .tail
assertAttr(instance=llist, attr="tail", value=Node(1))
# .head.data

# .size
assertAttr(instance=llist, attr="size", value=1)










