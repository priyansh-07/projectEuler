#gcd using euclidean algorithm
def gcd(a, b):
	if a==0:
		return b
	return gcd(b%a, a)

#standard formula for lcm
def lcm(a, b):
	return ( (a*b)/gcd(a,b) )

#lcm of n numbers = lcm(ans, n) ; ans = lcm(1,2,3,4,.....,n-1)
n=1
m=20
arr = [i for i in range(n, m+1)]
ans = arr[0]
for a in arr[1:]:
	ans = lcm(ans, a)
print(ans)