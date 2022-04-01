from enum import IntEnum
from exception_tree import TreeException
    
class TreeBST(object):
    """The base tree meant to be inherited from by other Binary Search Tree related
    structures (e.g. Red-Black or AVL). This Struct, while called TreeBST, is still
    a BST by itself and will work already.

    Raises:
        TreeException: If there are any errors that crop up, then this tree will throw
        a Tree-related Exception.
    """
    # Class Structs
    class TreeTraversalOrder(IntEnum):
        """A Traversal Order Enum to describe the three main traversal orders: 
        [PREORDER, INORDER, POSTORDER]
        """
        PREORDER  = 1 << 0,
        INORDER   = 1 << 1,
        POSTORDER = 1 << 2,

    class Node(object):
        """Generic Tree Node structure to contain necessary tree information.

        Data Members:
            value (object): The data to contain in the tree.
            
            left (Node): The left child of the current node.
            
            right (Node): The right child of the current node.
        """
        # Basic Tree Node structure
        def __init__(self, value=None, left=None, right=None) -> None:
            self.value = value
            self.left = left
            self.right = right
    
    # Class Members
    __null_node__ = Node()
    
    # Constructor
    def __init__(self) -> None:
        # Public
        self.count = 0
        
        # Private
        self.__root__ = None
    
    # Comparison Operators
    def __eq__(self, other: 'TreeBST') -> bool:
        # Equality based on whether self and other tree have the exact same structure
        def dfs(this_node: self.Node, other_node: self.Node) -> bool:
            # Accept when None case has been reached
            if not this_node:
                return True
            # If at any point that Nodes do not match, reject
            if this_node.value != other_node.value:
                return False
            
            # Recurse left then right and return overall truth value
            left = dfs(this_node.left, other_node.left)
            right = dfs(this_node.right, other_node.right)
            return left and right

        # Call DFS on both tree roots
        return dfs(self.__root__, other.__root__)
    
    def __contains__(self, value: object) -> bool:
        # Iterate through tree until value is found
        return self.__find_node__(value) != self.__null_node__
    
    def similar(self, other: 'TreeBST') -> bool:
        """Whether two trees are similar based on the values. This will perform an
        inorder traversal on both trees to ensure that they contains the same values
        only.

        Args:
            other (TreeBST): Tree to compare to.

        Returns:
            bool: Result of whether both trees contain the same value
        """
        return self.inorder() == other.inorder()
    
    # Iterator
    def __iter__(self):
        raise TreeException(self.__class__.__name__, 'Iterator not implemented.')

    def __next__(self):
        raise TreeException(self.__class__.__name__, 'Iterator not implemented.')
    
    # Public Methods
    def insert(self, value: object) -> bool:
        """Insert the given value into the tree. Will ignore duplicate and None type values.

        Args:
            value (object): Value to insert.

        Returns:
            bool: Returns True if insertion was successful.
        """
        # If value is None type, ignore insert
        if value == None:
            return False
        
        # If value is already contained in the tree, ignore duplicate
        if self.__contains__(value):
            return False
        
        # Run helper insert function, set root to rebalanced root and increment count
        self.__root__ = self.__insert__(value, self.__root__,)
        self.count = self.count + 1
        return True
    
    def remove(self, value: object) -> bool:
        new_root = self.__remove__(value, self.__root__)
        if new_root and new_root != self.__null_node__:
            self.__root__ = new_root
            self.count = self.count - 1
            return True
        
        return False
    
    def clear(self) -> None:
        # Reset values
        self.count = 0
        self.__root__ = None
        
    def max(self) -> object:
        """Find max value contained in the tree.

        Returns:
            object: Max value found.
        """
        return self.__find_max__(self.__root__).value
    
    def min(self) -> object:
        """Find min value contained in the tree.

        Returns:
            object: Min value found.
        """
        return self.__find_min__(self.__root__).value
        
    # Helper (Private) Operations
    def __insert__(self, value: object, node: Node) -> Node:
        """A recursive insert helper function to insert the node into the tree. This is
        purely a helper method and isn't meant to be called outside of the class.

        Args:
            value (object): The item to insert into the tree.
            node (Node): The current node that we're at.

        Returns:
            Node: The newly inserted node.
        """
        # If our current node is None, insert value
        if node == None:
            return self.Node(value, balance_factor=0, height=0)
        
        # Insert value left if less than current node, otherwise insert right
        if value < node.value:
            node.left = self.__insert__(value, node.left)
        else:
            node.right = self.__insert__(value, node.right)
        return node
    
    def __remove__(self, value: object, node: Node) -> Node:
        """A recursive remove helper function to remove a node from the tree. This is
        purely a helper method and isn't meant to be called outside of the class.

        Args:
            value (object): The item to be removed from the tree.
            node (Node): The current node that we're at.

        Returns:
            Node: The removed node.
        """
        # Ensure we're at a node that exists
        if not node:
            return None
        
        # Recursively traverse the tree to find our value.
        # When our value is less, traverse left
        if value < node.value:
            left_child = self.__remove__(value, node.left)
            if not left_child:
                return None
            node.left = left_child
        # When our value is more, traverse right
        elif value > node.value:
            right_child = self.__remove__(value, node.right)
            if not right_child:
                return None
            node.right = right_child
        # We have found our value
        else:
            # Node has either one or no children
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node has both children
            else:
                # Swap the value of the successor into the node.
                successor = self.__find_min__(node.right)
                node.value = successor.value

                # Go into the right subtree and remove the leftmost node we
                # found and swapped data with. This prevents us from having
                # two nodes in our tree with the same value.
                replacement = self.__remove__(node.right, successor.value)
                if not replacement:
                    return None
                node.right = replacement
        
        return node
    
    def __find_node__(self, value: object) -> Node:
        """Iterates through the tree to find the matching node that contains
        the given value. This is purely a helper method and isn't meant to be
        called outside of the class.

        Args:
            value (object): The value to match.

        Returns:
            Node: The node found containing the matched value.
        """
        # Iterate through the tree to find the node
        current_node = self.__root__
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return current_node
        
        return self.__null_node__
    
    def __find_min__(self, node: Node) -> Node:
        """Iterates through the tree to find the node that contains the smallest value.
        This is purely a helper method and isn't meant to be called outside of the class.

        Args:
            node (Node): The current node.

        Returns:
            Node: The node that has the smallest value.
        """
        while node.left:
            node = node.left
        return node 
    
    def __find_max__(self, node: Node) -> Node:
        """Iterates through the tree to find the node that contains the largest value.
        This is purely a helper method and isn't meant to be called outside of the class.

        Args:
            node (Node): The current node.

        Returns:
            Node: The node that has the largest value.
        """
        while node.right:
            node = node.right
        return node
    
    # Traversals
    def traverse(self, node: Node, order: TreeTraversalOrder) -> 'list[Node]':
        # Ensure that current node exists, otherwise break out early
        if not node:
            return []
        
        # Traverse based on TreeTraversalOrder and return resultant list
        if order == self.TreeTraversalOrder.PREORDER:
            return [node.value] + self.traverse(node.left, order) + self.traverse(node.right, order)
        elif order == self.TreeTraversalOrder.POSTORDER:
            return self.traverse(node.left, order) + self.traverse(node.right, order) + [node.value]
        else:
            return self.traverse(node.left, order) + [node.value] + self.traverse(node.right, order)
        
    def preorder(self) -> 'list[Node]':
        return self.traverse(self.__root__, self.TreeTraversalOrder.PREORDER)
    
    def inorder(self) -> 'list[Node]':
        return self.traverse(self.__root__, self.TreeTraversalOrder.INORDER)
    
    def postorder(self) -> 'list[Node]':
        return self.traverse(self.__root__, self.TreeTraversalOrder.POSTORDER)
