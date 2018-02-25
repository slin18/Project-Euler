
#for outerrange in range(0,200000,10000)
factors = set()
for i in range(1,21):
	for j in range(2,i):
		if i%j == 0:
			factors.add(j)
print(factors)
factors.add(11)
factors.add(13)
factors.add(17)
factors.add(19)
factors.remove(10)
factors.remove(9)
factors.remove(4)
factors.remove(2)
print(factors)

product = 1
for i in factors:
	print(product, i)
	product*=i
	print(product)


counter = 0
for i in range(1,21):
	if product%i==0:
		#print(counter)
		counter+=1
	else: 
		print(i)
	if counter==20:
		print("Yippee")

