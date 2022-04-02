def heapsort(list: 'list[object]') -> 'list[object]':
    # Helper Ops
    def max_heapify(list, i, end):
        # Get children indices
        left = i*2
        right = i*2+1
        
        # Track max, max is either child or parent
        max = None
        if left < end and list[left] > list[i]:
            max = left
        else:
            max = i
        if right < end and list[right] > list[max]:
            max = right
            
        # If our max isn't our parent, then make the
        # swap with our max child and heapify again
        # (sift down)
        if max != i:
            list[i], list[max] = list[max], list[i]
            max_heapify(list, max, end)
    
    # Build Max-Heap
    parent_start = len(list) // 2
    for i in range(parent_start, -1, -1):
        max_heapify(list, i, len(list))
        
    # Build sorted array at end of current array
    end = len(list) - 1
    while end > 0:
        list[0], list[end] = list[end], list[0]
        end = end - 1
        
        # Heapify when not at final 2 elements
        if end != 1:
            max_heapify(list, 0, end)
        else:
            # Swap both elements only if necessary
            max_heapify(list, 0, end+1)

    # Return in-place list
    return list
            

if __name__ == '__main__':
    test = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    heapsort(test)
    print(test)
    
    li1 = [5,4,3,2,1]
    li2 = [1,2,3,4,5]
    li3 = heapsort(li1)
    print(li2, li3)
    assert(li2 == li3)
    
    li4 = [6,2,8,5,2,7,9,9,4,3,7,1,4]
    li5 = sorted(li4)
    li6 = heapsort(li4)
    print(li5, li6)
    assert(li5 == li6)
    
    li5 = [0,9,3,2,5,4,6,7,1,8]
    li6 = [0,1,2,3,4,5,6,7,8,9]
    li7 = heapsort(li5)
    print(li5, li7)
    assert(li6 == li7)