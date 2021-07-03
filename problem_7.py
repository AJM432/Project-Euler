
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(num**(1/2))+1):
        if num % x == 0:
            return False
    return True

num = 10001
def nth_prime(n):
    prime_count = 0
    i=2
    while True:
        if is_prime(i):
            prime_count += 1
        
        if prime_count == n:
            return i
        i+=1

print(nth_prime(num))