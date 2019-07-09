##
## Imprima la suma de la segunda columna.
##
txt = open('data.csv', 'r').readlines()
txt = [z.replace('\t',' ') for z in txt]
txt = [z.replace('\n','') for z in txt]
txt = [z.split(' ') for z in txt]
a = sum([int(z[1]) for z in txt[0:]])
print(a)



