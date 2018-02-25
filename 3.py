# LOL I THOUGHT IT TOLD ME TO FIND ALL PRIME FACTORS
# I TROLLED 
# if you plug in 12, you get 2,2,2,3,6,12
# basically have to guess which of those values of prime to answer the question

factors = []
def primeFactor(value): 
	#all factors that multiply to value are prime 3
	for i in range(2,value): 
		if value%i==0: 
			factors.append(i)
			primeFactor(int(i))
			primeFactor(int(value/i))
			factors.append(int(value/i))
			break
	return factors
factors=primeFactor(600851475143)
print(factors)

'''def isPrime(value):
	counter = 0
	if value == 1 or value == 2: 
		return True
	else: 
		for i in range(2,value):
			if value%i!=0:
				counter+=1
				#print(value,i,value%i,counter)
		if counter == value-2:
			return True
		else:
			return False 
	return isPrime

print(isPrime(13))
#print(3%2)
true_factors = []
for i in range(len(factors)):
	if isPrime(factors[i]):
		true_factors.append(factors[i])

print(true_factors)'''

