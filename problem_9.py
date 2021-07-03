

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

range_=2000
for x in range(range_):
    for y in range(range_):
        c = (x**2+y**2)**(1/2)
        if c.is_integer():
            if x+y+int(c) == 1000:
                print(x*y*c)