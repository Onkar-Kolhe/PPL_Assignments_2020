
fd = open("/etc/hosts", "w")
l = {'coep':'www.coep.org.in', 'youtube':'www.youtube.com', 'facebook':'www.facebook.com', 'google':'www.google.com', 'linkedin':'www.linkedin.com'}

s = str(input("Enter the name of the website to be blocked(URL not necessary): "))
flag = 0
for i in l:
	if i.find(s) != -1 or l[i].find(s) != -1:
		
		print ("Blocked " + l[i])		
		fd.write("127.0.0.1 "+l[i]+ "\n")
		flag = 1

if flag == 0:
	print ("Couldn't block the website!")
	
fd.close()
