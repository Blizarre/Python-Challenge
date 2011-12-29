# http://www.pythonchallenge.com/pc/return/romance.html

import urllib2, urllib

urlCoo = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
#print urlCoo.info()

aut=urllib2.HTTPBasicAuthHandler() 
cook = urllib2.HTTPCookieProcessor()

aut.add_password(realm="inflate",  
uri="http://www.pythonchallenge.com",
user='huge', 
passwd='file') 
opener=urllib2.build_opener(aut, urllib2.HTTPHandler(debuglevel=1), cook) 
print opener.open(urlCoo)

# Cookie : info=you+should+have+followed+busynothing...;

def getNext(number=""):
	data_GET = urllib.urlencode({"busynothing":number})
	resultat = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?" + data_GET)
	print resultat.headers["Set-Cookie"]
	resultat = resultat.read()
	print resultat
	return float(resultat.split()[-1])


currentNum = getNext()

while(currentNum):
	currentNum = getNext(currentNum)
	
	
