# write a solution to bring steps down to 1 by dividing by 2 or adding 1 or subtracting 1 at each step

def answer(n):
	steps=0
	n=int(n)
	while not n==1:
		if n%2==0:
			steps+=1
			n=n//2
		elif n==3:
			steps+=2
			n=1
		else:
			steps+=3
			if (n+1)%4==0:
				n=n+1
			else:
				n=n-1
			n=n//4
	return steps
	

print answer("27")			
					
