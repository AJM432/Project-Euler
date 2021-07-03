
def fib(nth):
	a = 0
	b = 1
	c=0
	for x in range(1, nth+1):
		a = b
		b = c
		c = a+b
	return c


f = 0
i=0
while len(str(f)) < 1000:
	i+=1
	f = fib(i)

print(i)