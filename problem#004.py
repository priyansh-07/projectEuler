def palindrome(num):
	og=num
	num = str(num)
	og = str(og)
	if og==num[len(num)::-1]:
		return True
	return False

p=[]
m=999
product=0
while m>99:
	n=999
	while n>99:
		product = m*n
		if palindrome(product):
			p.append(product)
			break
		n-=1
	m-=1
print(max(p))