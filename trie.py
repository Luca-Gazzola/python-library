from exception_trie import TrieException

class Trie(object):
    """A tree-like data structure that contains words/strings. They are
    ordered by likeness and closeness to other existing words in the Trie
    """
    # Constant
    ALPHABET_SIZE = 26

    # Structs
    class Node(object):
        """Simple node to contain necessary info for the individual
        letters of the Trie. Children's indices refers to the letters
        in the alphabet.
        """
        def __init__(self) -> None:
            """Constructor that initializes then node whose children's 
            indices refer to the alphabet (lower case) -> Trie.ALPHABET_SIZE.
            """
            self.is_terminal = False
            self.children = [None for _ in range(Trie.ALPHABET_SIZE)]
        
    # Constructor
    def __init__(self):
        """Constructor that initializes the Trie structure.
        """
        self.__head__ = self.Node()
        
    # Operator Overrides
    def __contains__(self, string: str) -> bool:
        """Determines whether or not a given string exists with the Trie.

        Args:
            string (str): String to check existence in the Trie.

        Returns:
            bool: True if the string does exist.
        """
        # Start at head and incrementally get deeper
        node = self.__head__
        for depth in range(len(string)):
            # Get index at current string value
            index = self.__to_index__(string[depth])
            
            # If we meet a divergent path or non-existent entry, abort
            if not node.children[index]:
                return False
            
            # Go deeper until we find the end or abort early
            node = node.children[index]
        
        # If we're at the end, make sure that where we're at is actually
        # the end of the word (e.g. string="in" but we have "inn" -> False)
        return node.is_terminal
    
    def __str__(self) -> str:
        """Recursively prints all words contained in the Trie.

        Returns:
            str: All words found in the Trie (that are null-terminated).
        """
        def dfs(node: 'self.Node', path: str) -> 'list[str]':
            # If we reached the end of this branch, save word
            if node.is_terminal:
                return [path]

            # If there are any branches, cover paths them
            result = []
            for index, child in enumerate(node.children):
                if child:
                    result.extend(dfs(child, path + self.__to_char__(index)))
            
            return result
        
        result = []
        children = self.__head__.children
        for index, child in enumerate(children):
            if child:
                result.extend(dfs(child, f"{self.__to_char__(index)}"))
        
        return "[" + ", ".join(result) + "]"
        
    # Public Methods
    def insert(self, string: str) -> None:
        """Insert the given string into the Trie.

        Args:
            string (str): String to insert.

        Raises:
            TrieException: Raised if the string given is an invalid type.
        """
        # Check if valid string
        if not string or not isinstance(string, str):
            raise TrieException(__class__.__name__, f"String can't be inserted, incorrect type -> {string}: {type(string)}")
        
        # Start at head and check if index is taken
        node = self.__head__
        for depth in range(len(string)):
            # Convert current character to usable index
            index = self.__to_index__(string[depth])
            
            # If the index isn't taken by a Node, divergent path;
            # create new Node at given index
            if not node.children[index]:
                node.children[index] = self.Node()
            
            # Set current node to next practical node given our
            # index (if character already existed, just iterate;
            # if character didn't, the newly added Node will now
            # show the character)
            node = node.children[index]
        
        # Set final Node as our terminal node
        node.is_terminal = True
    
    def remove(self, string: str) -> None:
        """Removes the given string from the Trie.

        Args:
            string (str): String to remove.

        Raises:
            TrieException: Raised if the string given is an invalid type.
        """
        # Check if valid string
        if not string or not isinstance(string, str):
            raise TrieException(__class__.__name__, f"String can't be removed, given string is of incorrect type. -> {string}: {type(string)}")
  
        # Call recursive remove method
        self.__remove__(self.__head__, string)
        
    
    def clear(self) -> None:
        """Gets rid of all words current in a Trie, effectively resets the structure.
        """
        self.__head__ = self.Node()
    
    # Private Helper Methods
    def __to_index__(self, character: str) -> int:
        """Converts a given character to an index-able value: [0, 26). This
        method is not meant to be called outside of the class.

        Args:
            character (str): Character to convert.

        Raises:
            TrieException: Raised if the given character isn't a string of the
            appropriate length (a character is an isolated letter whose length
            is 1 -> 'a' is a character but 'ab' is not)

        Returns:
            int: Index value offset by the unicode value for 'a'.
        """
        if len(character) != 1:
            raise TrieException(__class__.__name__, "Character can't be indexed, not appropriate length.")
        return ord(str.lower(character)) - ord('a')
    
    def __to_char__(self, index: int) -> str:
        """Converts a given index value to a character based on unicode. This
        method is not meant to be called outside of the class.

        Args:
            index (int): Index to convert.

        Raises:
            TrieException: Raised if the given index isn't within the index-able
            alphabet range [0, 26).

        Returns:
            str: The character whose value is offset by the value for 'a'.
        """
        if index < 0 or index >= Trie.ALPHABET_SIZE:
            raise TrieException(__class__.__name__, f"Can't convert given integer ({index}) to a valid character.")
        return chr(index + ord('a'))
    
    def __remove__(self, node: 'Node', string: str) -> 'Node':
        """A recursive helper remove function that removes the given string
        from the Trie. This method is not meant to be called outside of the
        class.

        Args:
            node (Node): Current node to modify.
            string (str): Reference string to iterate through.

        Returns:
            Node: The modified node if it exists or hasn't been removed.
        """
        # If no reference string is left, if terminal node gets
        # removed. If node isn't terminal, then node is likely
        # part of another word, so leave it alone and return early
        if not string:
            if node.is_terminal:
                node.is_terminal = False
            return None

        # Grab index to current portion of reference string
        index = self.__to_index__(string[0])
        
        # Set child of current node to return of the recursive remove.
        # Increment the reference string and (naturally) the depth of
        # the Trie until we have removed all nodes that are no longer
        # needed
        node.children[index] = self.__remove__(node.children[index], string[1:])
        return node
        

if __name__ == '__main__':
    trie = Trie()
    print(trie)
    
    trie.insert("Hello")
    print(trie)
    
    trie.insert("Hi")
    print(trie)
    
    trie.remove("Hi")
    print(trie)
    