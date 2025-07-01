from linkedlist import LinkedList, Node

def node_as_dict(data, prev=None, next=None):
    return {
        'type': type(Node(None)),
        'data': data,
        'prev': prev,
        'next': next
    }

_ = {
    'type': type(LinkedList()),
    'head': None,
    'tail': None,
    'size': 0
}

_["head"] = node_as_dict(1)

_["head"]["next"] = node_as_dict(2)

_["tail"] = node_as_dict(2)

# print(_)

def recursive_func(_dict):
    
    for k, v in _dict.items():
        print(f"Current key is <{k}>, and current value is <{v}>")
        
        if type(v) == dict:
            recursive_func(v)
            print("End of current key")
        
recursive_func(_)