#http://www.pythonchallenge.com/pc/return/5808.html

import PIL as p

import Image as m_im

im = m_im.open("challenge11.jpg")
pix = im.load()
(sX, sY) = im.size

for i in range(sX):
    for j in range(sY):
        if(j%2==1):
            if(i%2==0):
                pix[i, j]=(0,0,0);
        else:
            if(i%2==1):
                pix[i, j]=(0,0,0);
        


import ImageOps as m_imOp
import ImageFilter as m_imFi

im = m_imOp.autocontrast(im, cutoff=2)
im =  im.filter(m_imFi.MaxFilter(size=3))
im.save("challenge11_res.jpg")
