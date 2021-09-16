import sys

def get_second_smallest_element(array) :
    if len(array) < 2:
        return False

    first = second = sys.maxsize

    for i in range(0, len(array)):
        if i < first:
            second = first
            first = array[i]
        elif i < second:
            second = array[i]
    return second



print(get_second_smallest_element([1,3,4,2,5,6,2,7]))
print(get_second_smallest_element([1,1]))



def get_second_smallest_element_bad(array) :
    if len(array) < 2:
        return False
    array.sort()
    return array[1]

print(get_second_smallest_element_bad([1,3,4,2,5,6,2,7]))
print(get_second_smallest_element_bad([1,1]))
