def login():
	user= input("enter the user : ")
	if user == 'B.haydar':
		print('ok fount')
	else:
		print ('not fount')
		login()
login()
def log():
	password = input ('enter password : ')
	if password == 'b.hayder':
		print ('ok fount')
	else:
		print ('not fount')
		log()
log()
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("hayder.txt","r");
	link = raw_input("enter the url : ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "[ok] hayder Al-Issawi====> ",req_link

print \
"""
888888b.       888                             888                  
888  "88b      888                             888                  
888  .88P      888                             888                  
8888888K.      88888b.   8888b.  888  888  .d88888  8888b.  888d888 
888  "Y88b     888 "88b     "88b 888  888 d88" 888     "88b 888P"   
888    888     888  888 .d888888 888  888 888  888 .d888888 888     
888   d88P d8b 888  888 888  888 Y88b 888 Y88b 888 888  888 888     
8888888P"  Y8P 888  888 "Y888888  "Y88888  "Y88888 "Y888888 888     
                                      888                           
                                 Y8b d88P                           
                                  "Y88P"      
                       hayder Al-Issawi                      
                                                                    
 """

findAdmin()
