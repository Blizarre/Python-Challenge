# http://www.pythonchallenge.com/pc/return/cat.html

import datetime as d

listeAnnees = []

for diz in range(100):
    annee = 1006 + diz*10
    if(d.date(annee,1,26).weekday()==0):    # does the 29 of january exist exist for this year ???
                                            # Quick, Dirty and error-proof
        exist = True
        try:
            d.date(annee,2,29).weekday()
        except Exception, e:
            exist = False
        if exist:
            listeAnnees.append(annee)

print "Google me : 27 of january",  listeAnnees[-2]            
                