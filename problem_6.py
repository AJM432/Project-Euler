# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

# .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# returns the sum of the numbers from 1 to n
def sum_numbers_squared(n):
    return int((n*(n+1)/2)**2)

def sum_squares(n):
    return sum(x**2 for x in range(1, n+1))

n=100
print(sum_numbers_squared(n) - sum_squares(n))