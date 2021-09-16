


def fibonacci_rec(n):
    if n <= 0:
        return False
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print(fibonacci_rec(4))

def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        return False
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(6))