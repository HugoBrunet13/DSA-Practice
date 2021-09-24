#Efficient program to print all prime factors of a given number

import math

def prime_factor(n):
    factors = []

    divisor = 2 #lowest prime number

    while divisor <= n:
        print(divisor, n)
        if n % divisor == 0:
            factors.append(divisor)  # store divisor in list of prime factor
            n = n / divisor          # divide n by his first prime factor
        else:
            divisor += 1 #update divisor


    return factors


# def primeFactors(n):

#     factors = []
     
#     # Print the number of two's that divide n
#     while n % 2 == 0:
#         n = n / 2
#         factors.append(2)
#         print(n)
         
#     # n must be odd at this point
#     # so a skip of 2 ( i = i + 2) can be used
#     for i in range(3,int(math.sqrt(n)),2):
#         print(int(math.sqrt(n)))
#         # while i divides n , print i and divide n
#         while n % i== 0:
#             factors.append(i),
#             n = n / i
#             print(n)
             
#     # Condition if n is a prime
#     # number greater than 2
#     if n > 2:
#         print(n)

#     return factors

# print(prime_factor(630))



def primeFactors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n/2

    print(n) # n is odd
    # Every composite number has at least one prime factor less than or equal to square root of itself. 
    
    for i in range(3, int(math.sqrt(n)), 2):
        while n % i == 0:
            factors.append(i)
            n = n / i

    if n > 2:
        factors.append(n)

    return factors

print(primeFactors(630))

# print(prime_factor(500))
# print(prime_factor(12))



