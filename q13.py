##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
txt = open('data.csv', 'r').readlines()
txt = [z.replace('\t',' ') for z in txt]
txt = [z.replace('\n','') for z in txt]
txt = [z.split(' ') for z in txt]
p13 = [i[4].split(',') for i in txt]
p13 = [[z[4] for z in j]for j in p13]
p13 = [[int(j) for j in i]for i in p13]
letras = [z[0] for z in txt]
for i in range(len(letras)):
    print(str(letras[i])+","+ str(sum(p13[i])))