import math
n=600851475143
while n%2==0:
	n/=2
m = math.sqrt(n)

i=3
while i<=m:
	while n%i==0:
		n/=i
		print(i)
	i+=2

print(i)