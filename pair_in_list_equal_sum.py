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
    counter = dict(Counter(arr))
    print(counter)
    cpt = 0
    for val in arr:
        print('\n',val)
        complement = target - val
        print("complement: ", complement, "  counter[complement]: ", counter[complement])
        if counter[complement] and counter[complement] > 0:
            cpt +=1
            counter[complement] -= 1
            # counter[val] -= 1
        print(counter)
    return cpt


# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6 

print("Count of pairs is", getPairsCount(arr,
                                        n, sum))


# def getPairsCount(arr, n, sum):
 
#     count = 0  # Initialize result
 
#     # Consider all possible pairs
#     # and check their sums
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == sum:
#                 count += 1
 
#     return count
 
 
# # Driver function
# arr = [1, 5, 7, -1, 5]
# n = len(arr)
# sum = 6
# print("Count of pairs is",
#       getPairsCount(arr, n, sum))