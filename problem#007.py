import math
def checkPrime(num):
	if num==2:
		return True
	if num%2==0:
		return False
	else:
		i=3
		m = math.sqrt(num)
		while i<=m:
			if num%i==0:
				if i==1:
					i+=2
					continue
				return False
			i+=2
		return True

i, count = 3,1
while count<10001:
	if checkPrime(i):
		print(i)
		count+=1
	i+=2

print(count)