def mergesort(list: 'list[object]') -> 'list[object]':
    if len(list) > 1:
        # Get midpoint of list
        mid = len(list) // 2
        
        # Separate main list and recurse
        left = mergesort(list[:mid])
        right = mergesort(list[mid:])
        
        # Prepare return list and move values over
        return_list = []
        left_i = right_i = return_i = 0
        while left_i < len(left) and right_i < len(right):
            if left[left_i] <= right[right_i]:
                return_list.append(left[left_i])
                left_i = left_i + 1
                return_i = return_i + 1
            else:
                return_list.append(right[right_i])
                right_i = right_i + 1
                return_i = return_i + 1
        
        # Move leftover values if left/right list contains it
        while left_i < len(left):
            return_list.append(left[left_i])
            left_i = left_i + 1
            return_i = return_i + 1
        while right_i < len(right):
            return_list.append(right[right_i])
            right_i = right_i + 1
            return_i = return_i + 1
        
        # Return list fragment
        return return_list

    # Return entire auxilary list
    return list

if __name__ == '__main__':
    li1 = [5,4,3,2,1]
    li2 = mergesort(li1)
    print(li1, li2)
    assert(li1 != li2)
    
    li3 = [6,2,8,5,2,7,9,9,4,3,7,1,4]
    li4 = mergesort(li3)
    print(li3, li4)
    assert(li3 != li4)
    
    li5 = [0,9,3,2,5,4,6,7,1,8]
    li6 = [0,1,2,3,4,5,6,7,8,9]
    li7 = mergesort(li5)
    print(li5, li7)
    assert(li5 != li7)
    assert(li6 == li7)