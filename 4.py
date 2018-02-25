def palliproduct():
	my_list = []
	for i in range(100,1000):
		for j in range(100,1000):
			if str(i*j)==str(i*j)[::-1]:
				my_list.append(i*j)
	return max(my_list)
print(palliproduct())
