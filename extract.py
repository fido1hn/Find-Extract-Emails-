domains = ['bellsouth.net', 'att.net', 'sbcglobal.net']

emaillist = open('CoinMarketCap 3.1M.txt', 'r') #open the email list

newlist = open('extractedemails', 'a') #open the new list 

"""
print(emaillist.readline())
print(emaillist.readline())
"""

for line in emaillist:  #iterate through and split check and save to the new list 
	prop = line.strip().split('@')
	if prop[1] in domains:
		#print(line)
		newlist.write(line)

newlist.close()
print('Done')
