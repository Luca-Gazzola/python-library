from collections import namedtuple
from typing import NamedTuple
from exception_hash import HashException

class HashTableBase(object):
    # Class Struct
    class TableEntry(object):
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
    
    # Constructor
    def __init__(self, hash_function=None, max_size=32):
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
        raise HashException(self.__class__.__name__, "'__getitem__' method not implemented")
        
    # Comparison Operators
    def __contains__(self, key: object):
        raise HashException(self.__class__.__name__, "'__contains__' method not implemented")
    
    # Public Methods
    def insert(self, key: object, value: object) -> None:
        raise HashException(self.__class__.__name__, "'insert()' method not implemented")
    
    def remove(self, key: object) -> object:
        raise HashException(self.__class__.__name__, "'remove()' method not implemented")
    
    def clear(self) -> None:
        # Reset values
        self.count = 0
        self.max_size = self.__original_size__
        self.__table__ = [None for _ in range(self.max_size)]
        
    # Helper (Private) Methods
    def __resize__(self) -> None:
        raise HashException(self.__class__.__name__, "'__resize__' menthod not implemented")
    
    def __hash_function__(self, key: object) -> int:
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
