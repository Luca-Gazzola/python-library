from enum import IntEnum
from utils_hoare import quick_partition, quick_pivot

class QuickselectMethod(IntEnum):
    RECURSIVE = 0
    ITERATIVE = 1

def quickselect(list: 'list[object]', k: int, type: QuickselectMethod = QuickselectMethod.RECURSIVE) -> object:
    """Returns the kth smallest element in the list using either
    recursion or iteration (depending on what type is specified).

    Args:
        list (list[object]): List to query through.
        k (int): The kth smallest element to return.
        type (QuickselectMethod, optional): Quickselect implementation
        method to use`. Defaults to QuickselectMethod.RECURSIVE.

    Returns:
        object: The kth smallest element in the list.
    """
    def select_recurse(list, left, right, k):
        # Base case: We've found the kth smallest element
        if left == right:
            return list[left]
        
        # Grab pivot and partition list
        pivot = quick_pivot(list)
        pivot = quick_partition(list, left, right)
        
        if k == pivot:
            # Target found early
            return list[k]
        elif k < pivot:
            # Recurse left partition
            return select_recurse(list, left, pivot - 1, k)
        else:
            # Recurse right partition
            return select_recurse(list, pivot + 1, right, k)
    
    def select_iterate(list, left, right, k):
        # Iterate through list until we find the kth smallest element
        # or we've exhausted the list
        while left != right:
            # Grab pivot and partition list
            pivot = quick_pivot(list)
            pivot = quick_partition(list, left, right)
            
            if k == pivot:
                # Target found early
                return list[k]
            elif k < pivot:
                # Iterate through left partition
                right = pivot - 1
            else:
                # Iterate through right partition
                left = pivot + 1
        
        # Return the kth smallest element
        return list[left]
    
    if k < 1 or k > len(list):
        raise ValueError('k must be between 1 and len(list)')
    
    select = select_recurse if type == QuickselectMethod.RECURSIVE else select_iterate
    return select(list, 0, len(list) - 1, k-1)

if __name__ == '__main__':
    test = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    expected = 4
    found = quickselect(test, 5)
    print(expected, found)
    
    test2 = [0,2,4,6,8,10]
    expected = 4
    found = quickselect(test2, 3)
    print(expected, found)
