from exception_hash import HashException

class HashTableBase(object):
    """Base Hash Table implementation, only meant to be inherited. This has no default implementation
    other than a few common functions.
    """
    
    # Class Struct
    class TableEntry(object):
        """A generic Table Entry struct to hold key-value pairs
        """
        def __init__(self, key=None, value=None):
            """Constructor that sets key-value pairs.

            Args:
                key (object, optional): Key for our Table Entry. Defaults to None.
                value (object, optional): Value assigned to the Key. Defaults to None.
            """
            self.key = key
            self.value = value
    
    # Constructor
    def __init__(self, hash_function=None, max_size=32):
        """Constructor for the Hash Table, allows for custom version of the hash function
        used in the data structure.

        Args:
            hash_function (lambda, optional): Hashing function. Defaults to None.
            max_size (int, optional): Max size for our internal starting array. Defaults to 32.
        """
        # Private
        self.__table__ = [self.TableEntry() for _ in range(max_size)]
        self.__original_size__ = max_size
        
        # Public
        self.count = 0
        self.max_size = max_size
        
        if hash_function:
            self.__hash_function__ = hash_function
    
    # Operator Overloads
    def __getitem__(self, key: object) -> object:
        """Accessor operator [] override for get methods.

        Args:
            key (object): Key to get to obtain value.

        Returns:
            object: Value paired with the given key.
        """
        raise HashException(self.__class__.__name__, "'__getitem__' method not implemented")
    
    def __setitem__(self, key: object, value: object) -> None:
        """Accessor operator [] override for set methods.

        Args:
            key (object): Key value to set or overwrite.
            value (object): Value to pair with the given key.
        """
        self.insert(key, value)
        
    # Comparison Operators
    def __contains__(self, key: object) -> bool:
        """Comparison operator 'in' override. Check whether the give key is inside of the
        hash table.

        Args:
            key (object): Key to check.

        Returns:
            bool: True if the key is found inside the hash table.
        """ 
        raise HashException(self.__class__.__name__, "'__contains__' method not implemented")
    
    # Public Methods
    def insert(self, key: object, value: object) -> None:
        """Insert key-value pair into the hash table. The key will be hashed prior to insertion.
        If the count exceeds the max_size, resize table.

        Args:
            key (object): Key to insert and hash.
            value (object): Value assigned to the key as a pair.
        """
        raise HashException(self.__class__.__name__, "'insert()' method not implemented")
    
    def remove(self, key: object) -> object:
        """Removes key-value pair from the hash table.

        Args:
            key (object): Key to remove.

        Returns:
            object: Returns the just removed key-value pair.
        """
        raise HashException(self.__class__.__name__, "'remove()' method not implemented")
    
    def clear(self) -> None:
        """Resets/clears all values from the hash table.
        """
        # Reset values
        self.count = 0
        self.max_size = self.__original_size__
        self.__table__ = [None for _ in range(self.max_size)]
        
    # Helper (Private) Methods
    def __resize__(self) -> None:
        """Resizes the given array and rehashes all values. This is a private function and should
        only be called internally.
        """
        raise HashException(self.__class__.__name__, "'__resize__' menthod not implemented")
    
    def __hash_function__(self, key: object) -> int:
        """Default implementation of the hash function. Takes care of most primitive types.

        Args:
            key (object): Key to hash.

        Raises:
            HashException: Raised if the provided key is of NoneType.

        Returns:
            int: Hash code to use derived from the key.
        """
        key_type = type(key)
        if key_type is int:
            return key % self.max_size
        elif key_type is float:
            front = int(key)
            back = int((key - front) * 10)
            return (front * 2 + back * 3) % self.max_size
        elif key_type is complex:
            real = int(key.real)
            imag = int(key.imag)
            return (real * 2 + imag * 3) % self.max_size
        elif key_type is str:
            sum = 0
            for c in key:
                sum = sum * 23 + int(c)
            return sum
        elif key_type is None:
            raise HashException(self.__class__.__name__, "Key is of type None, can not hash NoneType key.")
        else:
            return id(key) % self.max_size
