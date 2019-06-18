##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
txt = open('data.csv', 'r').readlines()
txt = [z.replace('\t',' ') for z in txt]
txt = [z.replace('\n','') for z in txt]
txt = [z.split(' ') for z in txt]
c1 = [z[0] for z in txt] #Columna 1
c2 = [z[3].split(',') for z in txt] #Columna 4
c3 = [z[4].split(',') for z in txt] #Columna 5
for z in range(len(c1)):
    print(str(c1[z])+","+ str(len(c2[z]))+","+ str(len(c3[z])))