def sumNatural(threshold):
	sumNat = 0
	for i in range(threshold):
		if i % 3 == 0 or i % 5 ==0:
			sumNat+=i
	return sumNat
print(sumNatural(1000))