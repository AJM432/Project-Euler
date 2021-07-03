

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def collatz(num):
	if num % 2 == 0:
		return num//2
	return 3*num+1


def collatz_sequence(num):
	count = 1
	new_num = num
	while new_num != 1:
		count += 1
		new_num = collatz(new_num)
	return count


largest_chain = 0
largest_chain_num = 0
sequence_val = 0
for x in range(1, 1000000):
	sequence_val = collatz_sequence(x)
	if sequence_val > largest_chain:
		largest_chain = sequence_val
		largest_chain_num = x

print(largest_chain_num)