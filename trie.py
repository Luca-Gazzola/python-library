class Trie(object):
    
    class Node(object):
        def __init__(self, value = None, children = []):
            self.value = value
            self.is_terminal = value == '\0'
            self.children = children
        
    def __init__(self):
        self.__head__ = self.Node()
    


if __name__ == '__main__':
    trie = Trie()
    