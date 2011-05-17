# coding:utf-8

# http://www.pythonchallenge.com/pc/return/bull.html

a = [1, 11, 21, 1211, 111221]

def transform(a):
    out = []
    nb = 1
    for n, e in enumerate(a):
        if nb > 1: # sert à retirer les caractères utilisés précédemment
            nb -= 1
        else:
            while n + nb < len(a) and a[n+nb] == e:
                nb+=1
            out.append(nb)
            out.append(e)

    return out


val = [1]
print val
for i in range(30):
    val = transform(val)
    print len(val)
    