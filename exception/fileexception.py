while 1:
	file = input("Enter the correct filename : \n")
	try:
		flcontent = open(file, 'r')
		content = flcontent.read()
	except IOError:
		print("File not Found\n")
	else:
		print("File content:\n {}".format(content))
		break	

