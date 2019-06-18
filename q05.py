##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
txt = open('data.csv', 'r').readlines()
txt = [z.replace('\t',' ') for z in txt]
txt = [z.replace('\n','') for z in txt]
txt = [z.split(' ') for z in txt]
x = sorted(set([z[0] for z in txt[0:]]))
for i in x:
    a = max([int(z[1]) for z in txt if z[0] == i])
    b = min([int(z[1]) for z in txt if z[0] == i])
    print(str(i)+","+ str(a)+","+ str(b))
