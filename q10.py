##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
txt = open('data.csv', 'r').readlines()
txt = [z.replace('\t',' ') for z in txt]
txt = [z.replace('\n','') for z in txt]
txt = [z.split(' ') for z in txt]
dic = [z[4].split(',') for z in txt]
dic = [[j[:3] for j in i] for i in dic]
dic = sum(dic, [])                       
dic_or = sorted(set(dic))                
for i in dic_or:
    a = [z for z in dic if z == i].count(i)
    print(str(i)+","+ str(a))