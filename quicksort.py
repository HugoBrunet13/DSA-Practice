# Python3 implementation of QuickSort

#Best	O(n*log n)
# Worst	O(n2)
#Average	O(n*log n)


def quicksort(sequence) :
    if len(sequence) < 1:
        return sequence
    else:
        pivot = sequence.pop()  # use last elements of sequence as the pivot

    items_lower = []            # list to store items lower than pivot
    items_greater = []          # list to store items greater than pivot


    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


test = [1,2,6,3,7,9,5,3,6,7,3,3,5,3,22,3,4,5,6,7,8,12,4,5,55,5,1,0]

print(quicksort(test))
