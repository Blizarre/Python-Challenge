# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpclib

a = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")


for m in a.system.listMethods():
    print m, a.system.methodSignature(m)
    print    a.system.methodHelp(m)
    print ""
    
next = a.phone("Bert") # see http://www.pythonchallenge.com/pc/return/evil4.jpg from challenge 12

print ">>>", next.split("-")[-1], "<<<"