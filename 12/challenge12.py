#! /usr/bin/env python

# http://www.pythonchallenge.com/pc/return/evil.html

from itertools import islice

with open("evil2.gfx", "rb") as fdIn:
    data = fdIn.read()
    for i in range(5):
        with open("out%d.dat"%(i,), "wb") as fdOut:
            fdOut.write( "".join(islice(data, i, None, 5))  )
