import math
def checkPrime(num):
	if num==2:
		return True
	if num%2==0:
		return False
	i=3
	m = math.sqrt(num)
	while i<=m:
		if num%i==0:
			return False
		i+=2
	return True

i = 3
sum=2
while i<2000000:
	if checkPrime(i):
		sum+=i
	i+=2
print(sum)