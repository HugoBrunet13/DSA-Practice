
# O(n) solution for finding smallest
# subarray with sum greater than x
 
# Returns length of smallest subarray
# with sum greater than x. If there
# is no subarray with given sum, then
# returns n + 1
 
 
def smallestSubWithSum(arr, n, x):
 
    # Initialize current sum and minimum length
    curr_sum = 0
    min_len = n + 1
 
    # Initialize starting and ending indexes
    start = 0
    end = 0
    while (end < n):
 
        # Keep adding array elements while current
        # sum is smaller than or equal to x
        while (curr_sum <= x and end < n):
            curr_sum += arr[end]
            end += 1    
            print("curr_sum: %s, end: %s"%(curr_sum, end))
            
        print("\nStop, curr_sum: ", curr_sum)
        # If current sum becomes greater than x.
        while (curr_sum > x and start < n):
            
            # Update minimum length if needed
            if (end - start < min_len):
                min_len = end - start
                print("min_len: ",min_len)
 
            # remove starting elements
            curr_sum -= arr[start]
            start += 1
            print("curr_sum: %s, start: %s"%(curr_sum, start))

        print("\n")

    print("Sum:", curr_sum)
    return min_len
 
 
# Driver program
arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubWithSum(arr1, n1, x)
print("Not possible") if (res1 == n1 + 1) else print(res1)