
# find sum of all multiples of 3 and 5 below 1000
multiple = []

for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        print(x)
        multiple.append(x)

print(sum(multiple))
