n = int(input("Enter the integer \n"))
d=2
while(n!=0):
	if(n%d !=0):
		d+=1
	else:
		n=n/d
		if(n==1):
			print("The largest prime factor is : " , d)