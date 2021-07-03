import os
from string import ascii_uppercase



def letter_val(letter):
	return ascii_uppercase.index(letter.upper()) + 1


def name_val(name):
	return sum([letter_val(x) for x in name])




with open(os.path.join("Assets", "names.txt"), 'r') as file:
	data = file.read()

data = sorted(data.strip().split(','))
total = 0
for index, name in enumerate(data):

	total += name_val(name[1:-1]) * (index+1)

print(total)