a = 1

def multiply(a, n):
	if type(n) is not int:
		return
	def multiply_by_n():
		print(a)
		print(n)
		return a*n

b = 2
print(multiply(b, 3))
print(a)

print (type(multiply))
print (type(multiply_by_n))