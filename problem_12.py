
import time
from collections import Counter
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?


def num_factors_old(num):
    # factors = 0
    # for x in range(1, num+1):
    #     if num % x == 0:
    #         factors += 1
    # return factors
    return len([x for x in range(1, num+1) if num % x == 0])


def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(num**(1/2))+1):
        if num % x == 0:
            return False
    return True


# calculates the nth triangle number
def triangle_num(n):
    return int(n*(n+1) / 2)

def prod(array):
    product = 1
    [product := product * x for x in array]
    return product
    
def prime_factorization(num):
    prime_fac = []
    left_over = num
    while int(prod(prime_fac)) != num:
        for x in range(2, int(left_over+1)):
            if is_prime(x) and left_over%x==0:
                prime_fac.append(x)
                left_over /=x
                break
    return prime_fac


def number_of_factors(num):
    product = 1
    [product := product*(x+1) for x in Counter(prime_factorization(num)).values()]
    return product


i=1
while True:
    if number_of_factors(triangle_num(i)) > 500:
        print(triangle_num(i))
        break
    i+=1