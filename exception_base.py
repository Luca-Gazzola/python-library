class PythonLibraryException(Exception):
    def __init__(self, __namespace__, __classname__, message):
        self.__namespace__ = __namespace__
        self.__classname__ = __classname__
        self.message = message

    def __str__(self):
        return f"Python-Library ({self.__namespace__} | {self.__classname__}): {self.message}"
