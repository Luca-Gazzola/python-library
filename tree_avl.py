from turtle import left
from tree_base import *

class AVLTree(BaseTree):
    """An AVL Tree that inherits from the Base Tree (BST) class. Self-balances as you
    insert and remove to ensure faster access times.
    """
    # Class Structs
    class Node(BaseTree.Node):
        """An AVL Node that inherits from the Base Tree (BST) class. Has additional
        structural data to allow for AVL operations.
        """
        # Use BaseTree.Node as our basis, add AVL specific fields
        def __init__(self, value=None, left=None, right=None, balance_factor=None, height=None) -> None:
            super().__init__(value, left, right)
            self.balance_factor = balance_factor
            self.height = height
    
    # Constructor
    def __init__(self) -> None:
        super().__init__()
    
    # Helper Operations
    def __insert__(self, value: object, node: Node) -> Node:
        """A recursive insert helper function to insert the node into the tree. This is
        purely a helper method and isn't meant to be called outside of the class.

        Args:
            value (object): The item to insert into the tree.
            node (Node): The current node that we're at.

        Returns:
            Node: The balanced node after insertion has occurred, may or may not be the
            recently inserted node.
        """
        # If our current node is None, insert value
        if node == None:
            return self.Node(value, balance_factor=0, height=0)
        
        # Insert value left if less than current node, otherwise insert right
        if value < node.value:
            node.left = self.__insert__(value, node.left)
        else:
            node.right = self.__insert__(value, node.right)
        
        # Update node data and restructure tree if necessary
        self.__update_node__(node)
        return self.__balance_tree__(node)
    
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
                # Remove from left child
                if node.left.height > node.right.height:
                    # Swap the value of the successor into the node.
                    successor = self.__find_max__(node.left)
                    node.value = successor.value

                    # Find and replace largest value in the left child
                    replacement = self.__remove__(successor.value, node.left)
                    if not replacement:
                        return None
                    node.left = replacement
                else:
                    # Swap the value of the successor into the node.
                    successor = self.__find_min__(node.right)
                    node.value = successor.value

                    # Find and replace the smallest value in the right child
                    replacement = self.__remove__(successor.value, node.right)
                    if not replacement:
                        return None
                    node.right = replacement
        
        # Update and rebalance nodes
        self.__update_node__(node)
        return self.__balance_tree__(node)
    
    # AVL Operations
    def __balance_tree__(self, node: Node) -> Node:
        """A balancing operation conducted on a given node. Will do appropriate rotations
        to the AVL Tree to maintain balance. This is a helper function not meant to be
        called outside of the class.

        Args:
            node (Node): Node to run balancing on.

        Returns:
            Node: The newly balanced center node. May or may not be the same node passed
            as the parameter.
        """
        # Left-heavy tree
        if node.balance_factor <= -2:
            # Check balance factor of left child to verify rotation case
            if node.left.balance_factor <= 0:
                # LL Case
                return self.__rotate_right__(node)
            else:
                # LR Case
                node.left = self.__rotate_left__(node.left)
                return self.__rotate_right__(node)
        
        # Right-heavy tree
        if node.balance_factor >= 2:
            # Check balance factor of right child to verify rotation case
            if node.right.balance_factor >= 0:
                # RR Case
                return self.__rotate_left__(node)
            else:
                # RL Case
                node.right = self.__rotate_right__(node.right)
                return self.__rotate_left__(node)
        
        # Balance factor is ok, return node
        return node
    
    def __update_node__(self, node: Node) -> None:
        """Updates given node's AVL data to maintain balance (height and balance_factor).

        Args:
            node (Node): Node to update.
        """
        # Init children heights
        left_height = -1
        right_height = -1
        
        # Grab children node heights
        if node.left:
            left_height = node.left.height
        if node.right:
            right_height = node.right.height
        
        # Update this node's height
        node.height = 1 + max(left_height, right_height)
        
        # Update balance factor
        node.balance_factor = right_height - left_height
    
    # AVL Rotations
    def __rotate_left__(self, node: Node) -> Node:
        # Rotate nodes to the left
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        
        # Update necessary nodes
        self.__update_node__(node)
        self.__update_node__(right_child)
        return right_child
    
    def __rotate_right__(self, node: Node) -> Node:
        # Rotate nodes to the right
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        
        # Update necessary nodes
        self.__update_node__(node)
        self.__update_node__(left_child)
        return left_child
        
        
   

if __name__ == '__main__':
    # Driver program to test above function
    myTree = AVLTree()
    
    myTree.insert(10)
    myTree.insert(20)
    myTree.insert(30)
    myTree.insert(40)
    myTree.insert(50)
    myTree.insert(25)
    
    """
    The constructed AVL Tree would be
             30
            /  \
           20   40
          /  \    \
         10  25    50
    """
    
    # Preorder Traversal
    print("Preorder traversal of the",
        "constructed AVL tree is")
    print(myTree.preorder())
    
    # Inorder Traversal
    print("Inorder traversal of the",
        "constructed AVL tree is")
    print(myTree.inorder())
    
    # Postorder Traversal
    print("Postorder traversal of the",
        "constructed AVL tree is")
    print(myTree.postorder())
    
    # Operations check
    print("Check comparisons")
    otherTree = AVLTree()
    otherTree.insert(10)
    otherTree.insert(20)
    otherTree.insert(30)
    otherTree.insert(40)
    otherTree.insert(50)
    otherTree.insert(25)
    print("Are Equal:", myTree == otherTree)
    print("Are Similar:", myTree.similar(otherTree))
    print("Contains 10:", 10 in myTree)
    
    # Removals
    myTree.remove(30)
    print(myTree.inorder())
