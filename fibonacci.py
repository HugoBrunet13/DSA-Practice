


def fibonacci_rec(n):
    if n <= 0:
        return False
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

# print(fibonacci_rec(4))

def fibonacci_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    res = [None] * (n +1)
    res[1]=1
    res[2]=1
    for i in range(3, n+1):
        res[i]= res[i-1]+res[i-2]
    return res[n]

print(fibonacci_bottom_up(10000))