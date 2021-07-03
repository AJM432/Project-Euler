

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# could not complete for loop because it did not check if number was greater than previous, fix later or never

a = max([x*y for x in range(100, 999) for y in range(100, 999) if str(x*y) == str(x*y)[::-1]])
print(a)
# print(a)
# largest = 0
# prev = 0
# for x in range(100, 1000):
#     for y in range(100, 1000):
#         product = x*y
#         if str(x*y) == str(x*y)[::-1] and largest > prev:
#             prev = largest
#             largest = product

# print(largest)
