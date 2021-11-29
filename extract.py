domains = ['yahoo.com', 'gmail.com', 'outlook.com'] #Domains that you want to extract from the file 

emaillist = open('10kmixedemaillist', 'r') #open your email list in read mode

newlist = open('extractedemails', 'a') #open the new list in append mode

"""
print(emaillist.readline())	#This was for debugging
print(emaillist.readline())	#More debugging
"""

for line in emaillist:  #iterate through the file
	prop = line.strip().split('@')		#Strip the line of space and split it
	if prop[1] in domains:			#check if domain is in our list 
		#print(line)			#Debugging
		newlist.write(line)		#Add to new file

newlist.close()					#Close the file
print('Done')					#Give us feedback
