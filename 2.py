#1,1,2,3,

def fib(n):
    fib_list = [1,1]
    for i in range(n):
    	if i >= 2:
    		fib_list.append(fib_list[i-2]+fib_list[i-1])  
    return fib_list

last_i = 0
for i in range(100): 
	fib_list=fib(i)
	if fib_list[i-1] < 4000000:
		last_i = i

## found that it was 33
fib_list=fib(last_i)
even_list = []
for i in range(len(fib_list)):
	if fib_list[i]%2==0:
		even_list.append(fib_list[i])
print(sum(even_list))