sum = 0
c = 0
a=1
b=2
def fib(a,b):
	return a+b

while(b<400000):
	if b%2==0:
		sum=sum+b
	c=fib(a,b)
	a=b
	b=c

print(sum)


	