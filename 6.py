def sumSquare(value):
	sumSquare = 0
	sqSum = 0
	for value in range(1,value+1): 
		sumSquare+=value**2
		sqSum+=value
	return sqSum**2 - sumSquare

print(sumSquare(100))