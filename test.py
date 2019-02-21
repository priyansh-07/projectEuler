def gcd(a, b):
	lower=int()
	higher=int()
	lcm = int()
	if a<=b:
		lower=a
		higher=b
	else:
		lower=b
		higher=a
	i=1
	while i<=lower:
		if lower%i==0 and higher%i==0:
			lcm = i
		i+=1
	return lcm


gcd(2,4)