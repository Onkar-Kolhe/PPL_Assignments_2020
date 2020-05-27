# Zero division error Exception

q = int(input("Enter dividend "))
while 1:
	try:
		p = int(input("Enter divisor "))
		result = q / p
	except ZeroDivisionError:
		print("ZeroDivisionError : Enter the divisor again\n")
	else:
		print("Result = {} \n".format(result))
		break
# Index error
try:
	l = [ 2,3,4,1,8,7]
	print(l[9])
except LookupError:
	print("LookupError : Index error ocurred\n")
else:
	print("No error\n ")

# Assertion Error
try:
	a = 37.37
	b = 'Capital'
	assert a == b
except AssertionError:
	print("AssertionError : AssertionError occured\n")
else:
	print("No error\n ")

# KeyboardInterrupt Exception
try:
	ip = input("Press Ctrl+C or Interrupt Kernel\n")
except KeyboardInterrupt:
	print("KeyboardInterrupt Exception occured \n")
else:
	print("No error\n")
