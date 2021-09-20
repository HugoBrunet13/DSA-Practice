
# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.


# O(n^3) (call 3 recursive method)
def find_ways(n):
    if n == 0 or n == 1:
        return 1
    elif n== 2:
        return 2
    else:
        return find_ways(n-1) + find_ways(n-2)+find_ways(n-3)

# O(n) only on tracersal
def find_ways_dyn(n):
    res = [0] * (n + 1)  # init array of size n+1
    res[0] = 1 # init with base case ; 1 way to get to floor 0
    res[1] = 1 # 1 way to go to floor 1
    res[2] = 2 # 2 way to go to floor 2
    # print(res)
    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
        # print(i, res)

 
    return res[n]
 
print(find_ways_dyn(25))
print(find_ways(25))
