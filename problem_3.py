
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


# key takeaway: you only have to check up to sqrt(num) because the factors a*b that compose num each cannot exceed sqrt(num) because a*b would be greater than num
def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(num**(1/2))+1):
        if num % x == 0:
            return False
    return True


def largest_prime(num):
    remaining = num
    largest = 0
    for x in range(2, int(num**(1/2))):
        if is_prime(x) and remaining%x==0:
            largest = x
            remaining = remaining / x
    return largest


print(largest_prime(600851475143))