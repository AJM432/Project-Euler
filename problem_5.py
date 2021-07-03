import numpy as np


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple():
    i=1
    while True:
        if i%20 == 0:
            if all([i%x==0 for x in range(2, 20)]):
                return i
        i+=1

print(smallest_multiple())
