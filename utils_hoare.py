import random

def quick_pivot(list: 'list[object]') -> int:
    """Gives the median pivot of 3 random elements in the list

    Args:
        list (list[object]): List to be sorted.

    Returns:
        int: Index of the median pivot.
    """
    pivots = [random.randint(0, len(list) - 1) for _ in range(3)]
    x = pivots[0] - pivots[1]
    y = pivots[1] - pivots[2]
    z = pivots[0] - pivots[2]
    if x * y > 0:
        return pivots[1]
    if x * z > 0:
        return pivots[2]
    return pivots[0]

def quick_partition(list: 'list[object]', left: int, right: int) -> int:
    """Partitions and swaps the list based off of the pivot.

    Args:
        list (list[object]): List to be partitioned.
        left (int): Left index of the list.
        right (int): Right index of the list.

    Returns:
        int: Index of the pivot.
    """
    # Grab a pivot value that's semi-random to avoid worst case
    # scenarios (i.e. grab the median element of 3 random pivots)
    pivot = list[quick_pivot(list)]

    # Left/right indices
    start = left - 1
    end = right + 1

    # Loop until indices cross
    while True:
        # Move the left index to the right at least once and while the element at
        # the left index is less than the pivot
        start += 1
        while list[start] < pivot:
            start += 1
        
        # Move the right index to the left at least once and while the element at
        # the right index is greater than the pivot
        end -= 1
        while list[end] > pivot:
            end -= 1
        
        # If the indices crossed, return
        if start >= end:
            return end
        
        # Swap the elements at the left and right indices
        list[start], list[end] = list[end], list[start]
