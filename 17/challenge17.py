# http://www.pythonchallenge.com/pc/return/romance.html

import urllib2

urlCoo = "http://www.pythonchallenge.com/pc/return/cookies.html"
#print urlCoo.info()

aut=urllib2.HTTPBasicAuthHandler() 
cook = urllib2.HTTPCookieProcessor()

aut.add_password(realm="inflate",  
uri="http://www.pythonchallenge.com",
user='huge', 
passwd='file') 
opener=urllib2.build_opener(aut, urllib2.HTTPHandler(debuglevel=1), cook) 
print opener.open(urlCoo)#.read() 