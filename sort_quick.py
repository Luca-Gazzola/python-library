import random
from utils_hoare import quick_partition

def quicksort(list: 'list[object]') -> 'list[object]':
    """Quicksort implementation based off of Hoare's partition scheme.
    This is an unstable, in-place sort.

    Args:
        list (list[object]): List to be sorted.

    Returns:
        list[object]: Sorted list based off of Hoare's partition scheme.
    """
    def sort(list: 'list[object]', left: int, right: int):
        # Ensure that we have a valid condition to sort
        if left < right:
            pivot = quick_partition(list, left, right)
            sort(list, left, pivot)
            sort(list, pivot+1, right)
    
    sort(list, 0, len(list) - 1)
    return list
            

if __name__ == '__main__':
    test = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    quicksort(test)
    print(test)
    
    li1 = [5,4,3,2,1]
    li2 = [1,2,3,4,5]
    li3 = quicksort(li1)
    print(li2, li3)
    assert(li2 == li3)
    assert(li1 == li3) # ensure in-place
    
    li4 = [6,2,8,5,2,7,9,9,4,3,7,1,4]
    li5 = sorted(li4)
    li6 = quicksort(li4)
    print(li5, li6)
    assert(li5 == li6)
    assert(li4 == li6) # ensure in-place
    
    li5 = [0,9,3,2,5,4,6,7,1,8]
    li6 = [0,1,2,3,4,5,6,7,8,9]
    li7 = quicksort(li5)
    print(li5, li7)
    assert(li6 == li7)
    assert(li5 == li7) # ensure in-place
