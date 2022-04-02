from hash_table_base import *

class HashTableSC(HashTableBase):
    # Class Structs
    class TableEntry(HashTableBase.TableEntry):
        def __init__(self, node: 'ListNode' = None) -> None:
            self.node = node
        
    class ListNode(object):
        def __init__(self, key=None, value=None, prev=None, next=None) -> None:
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
    
    # Constructor
    def __init__(self):
        super().__init__()
        
    # Operator Overload
    def __getitem__(self, key: object) -> object:
        # Grab entry from table with hash
        entry = self.__table__[self.__hash_function__(key)]
        
        # Iterate through chain to find proper value
        node = entry.node
        while node:
            if node.key == key:
                return node.value
            node = node.next

        # If nothing found, raise not found exception
        raise HashException(self.__class__.__name__, f"{key} was not found, could not retrive value.")
        
    # Public Method
    def insert(self, key: object, value: object) -> None:
        hashed_code = self.__hash_function__(key)
        entry = self.__table__[hashed_code]
        if not entry.node:
            entry.node = self.ListNode(key, value)
        else:
            # Find the next available space in the chain
            node = entry.node
            while node.next:
                # Check if the key we're using is a duplicate, if so override
                # existing value
                if node.next.key == key:
                    node.value = value
                    return
                node.next = node.next.next
            
            # Check if current node is a duplicate value (this assumes only
            # one node exists in the TableEntry)
            if node.key == key:
                node.value = value
                return
            
            # Once found, add new node to the chain
            node.next = self.ListNode(key, value, prev=node)
        
        self.count = self.count + 1
        
    def remove(self, key: object) -> object:
        hashed_code = self.__hash_function__(key)
        entry = self.__table__[hashed_code]
        if entry.node:
            # Find the next available space in the chain
            node = entry.node
            while node:
                if node.key == key:
                    # Relink next/prev nodes to one another after this node's
                    # removal
                    if node.prev:
                        node.prev.next = node.next
                    else:
                        # No prev implies head of the list, so remove ListNode
                        # from TableEntry
                        entry.node = None
                    if node.next:
                        node.next.prev = node.prev
                    self.count = self.count - 1
                    return (node.key, node.value)
                node = node.next
        
        raise HashException(self.__class__.__name__, f"{key} was not found, could not remove value.")

if __name__ == '__main__':
    table = HashTableSC()
    table.insert(10, "Hello")
    print(table[10])
    assert(table.count == 1)
    
    try:
        table[20]
    except HashException:
        print("No found entry test: Pass")
        
    table.insert(42, "World")
    print(table[42])
    assert(table.count == 2)
    
    table[1] = "What's up?"
    print(table[1])
    assert(table.count == 3)
    
    print("Override existing entry")
    table[1] = "Not much, you?"
    print(table[1])
    assert(table.count == 3)
    
    print("Remove entry")
    table.remove(1)
    try:
        print("Found unremoved entry:", table[1])
        raise Exception("Test Incorrect")
    except HashException:
        print("Successfully removed")
    assert(table.count == 2)
