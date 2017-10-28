n=0
for x in range(999,100,-1):
	for y in range(999,100,-1):
		z=x*y
		if z>n:
			s=str(x*y)
			if s==s[::-1]:
				n=x*y
				
print("The largest palindrome is : " , n)				