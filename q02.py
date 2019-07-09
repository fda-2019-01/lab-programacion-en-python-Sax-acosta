##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
txt = open('data.csv', 'r').readlines()
txt = [z.replace('\t',' ') for z in txt]
txt = [z.replace('\n','') for z in txt]
txt = [z.split(' ') for z in txt]
x = sorted(set([z[0] for z in txt[0:]]))
c = [i[0] for i in txt]
for i in x:
    print(str(i)+","+ str(c.count(i)))