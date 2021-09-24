
def get_median_2_array_bad(arr1, arr2):
    arr3 = arr1 + arr2
    arr3.sort()  #nlog(n)

    if len(arr3) % 2 == 0:
        mid = len(arr3) // 2
        return (arr3[mid] + arr3[mid -1]) /2
    else:
        return arr3[len(arr3)//2]


arr1 = [ -5, 3, 6, 12, 15 ]
arr2 = [ -12, -10, -6, -3, 4, 10 ]

print("Median = ", get_median_2_array_bad(arr1, arr2))


