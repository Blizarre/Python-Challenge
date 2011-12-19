# http://www.pythonchallenge.com/pc/return/mozart.html

import Image

mozart = Image.open("mozart.gif")
mozart = mozart.convert("RGB")

nbCols, nbLignes = mozart.size

out = Image.new( mozart.mode , mozart.size)

pixMozart = mozart.load()
pixOut = out.load()


for numL in range(nbLignes):
	numC = 0
	while numC < nbCols and pixMozart[numC, numL] != (255,0,255):
		numC += 1

	debut = [ pixMozart[c, numL] for c in range(0, numC -1 ) ]
	fin = [ pixMozart[c, numL] for c in range(numC + 6, nbCols) ]
	fin.extend(debut)
	for c in range(nbCols-7):
		pixOut[c, numL] = fin[c]

out.save("out.png")

