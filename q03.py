##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
txt = open('data.csv', 'r').readlines()
txt = [z.replace('\t',' ') for z in txt]
txt = [z.replace('\n','') for z in txt]
txt = [z.split(' ') for z in txt]
x = sorted(set([z[0] for z in txt[0:]]))
for i in x:
    a = sum([int(z[1]) for z in txt[0:] if z[0] == i])
    print(str(i)+","+ str(a))