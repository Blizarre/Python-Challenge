# http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image as im
from numpy import array, zeros

wire = im.open("wire.png")
result = im.new(wire.mode, (100,100))

pixIn = array(wire.getdata())
pixOut = zeros((100,100,3))

old = 0 #contain the position of the last data used in pixIn
for level in range(50):
    pixOut[0+level:100-level, level, :]         = pixIn[old:old+100-level*2, :]
    old += 100 - level*2
    pixOut[99-level, 1+level:100-level, :]  = pixIn[old:old + 99 - level*2, :]
    old += 99 - level*2
    pixOut[0+level:99-level, 99-level, :]   = pixIn[old:old + 99 - level*2, :][::-1]
    old += 99 - level*2
    pixOut[0+level, 1+level:99-level, :]    = pixIn[old:old + 98 - level*2, :][::-1]
    old += 98 - level*2

    #pixOut[0:100, 0] = pixIn[:100]     #100
    #pixOut[99, 100:1] = pixIn[100:199] # 99
    #pixOut[99:0, 99] = pixIn[199:298]  # 99
    #pixOut[0, 99:1] = pixIn[298:396]   # 98

pixData = result.load()
for i in range(100):
    for j in range(100):
        pixel = tuple( int(k) for k in pixOut[i,j,:] ) # int needed for every color
        pixData[i,j] = pixel
result.save("result.png")