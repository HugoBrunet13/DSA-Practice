import math

def is_power(x, y):
    if y == 1:
        return True
    pow = 1
    while(pow < y):
        pow = pow * x
    return pow == y

def is_power_of_10(y):
    return math.log10(y).is_integer()

print(is_power_of_10(1))
print(is_power_of_10(10))
print(is_power_of_10(100))
print(is_power_of_10(1000))
print(is_power_of_10(10000))
print(is_power_of_10(100000))
print(is_power_of_10(10090))
print(is_power_of_10(8989900))


# print(is_power(10, 1))
# print(is_power(10, 10))
# print(is_power(10, 100))
# print(is_power(10, 1000))
# print(is_power(10, 10000))
# print(is_power(10, 100000))
# print(is_power(8989, 10090))
# print(is_power(10, 1050))



