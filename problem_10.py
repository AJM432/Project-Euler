

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(num**(1/2))+1):
        if num % x == 0: return False
    return True

max=2000000
print(sum([x for x in range(2, max+1) if is_prime(x)]))