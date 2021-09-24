# How many pairs of numbers are in the list which equal the sum?
# They run a series of numbers with a sum at the end, you’re then asked to develop a
# solution which finds how many pairs of numbers are in the list which equal the sum.

# Python 3 implementation of simple method
# to find count of pairs with given sum.
import sys
from collections import Counter

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'


def getPairsCount(arr, n, target):
    print(arr, target)
    cpt = 0
    res = []
    for val in arr:
        complement = target - val
        if complement in arr and {complement, val} not in res:
            res.append({val, complement})
            print(res)
            cpt +=1
    return cpt


# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6 

print("Count of pairs is", getPairsCount(arr,
                                        n, sum))
