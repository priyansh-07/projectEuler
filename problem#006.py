sumOfSquares=0
squareOfSum=0

for i in range(1, 101):
	sumOfSquares+=(i*i)
	squareOfSum+=i

print("difference = ", str(sumOfSquares-(squareOfSum*squareOfSum)))

print(sumOfSquares, "\n", squareOfSum)