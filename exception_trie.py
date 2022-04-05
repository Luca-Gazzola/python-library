from exception_base import PythonLibraryException

class TrieException(PythonLibraryException):
    def __init__(self, __classname__, message):
        super().__init__("Data Structures", __classname__, message)
