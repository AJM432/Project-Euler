# find the sum of even number in fibonachi sequence,
# greatest number cant exceed 4 million
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...


fib = []
fib_sum = []

x = 0
y = 1
z = 0

while z < 4_000_000:

    z = x + y
    fib.append(z)
    # update values
    x = y
    y = z
        
for x in fib:
    if x % 2 == 0:
        fib_sum.append(x)

print(sum(fib_sum))
