# coding:utf-8

# http://www.pythonchallenge.com/pc/return/bull.html

# the riddle's answer is really simple (and yet I haven't found it by myself :-/ ). Juste read the array "RLE-style" :
# 1        : one 1
# 11       : two 1
# 21       : one 2 one 1
# 1211     : one 1 one 2 two 1
a = [1, 11, 21, 1211, 111221]


def transform(a):
    """Return a translated version of the array ! => 112 becomes 2112 (two 1, one 2)"""
    out = []
    nb = 1 # number of digits of the same value
    for n, e in enumerate(a):
        if nb > 1: # discard digits that have been already used
            nb -= 1
        else:
            while n + nb < len(a) and a[n+nb] == e: # count the number of digits with same value
                nb+=1
            out.append(nb)
            out.append(e)

    return out


val = [1]

for i in range(30): val = transform(val)

print "len(val[30]) =", len(val)