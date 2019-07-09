##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
txt = open('data.csv', 'r').readlines()
txt = [z.replace('\t',' ') for z in txt]
txt = [z.replace('\n','') for z in txt]
txt = [z.split(' ') for z in txt]
let = [line[3].split(',') for line in txt]
let_or = sorted(set(sum(let,[])))
ho = [line[1:4] for line in txt]
a = []
for line in ho:
    a.append([line[0]] + line[2].split(','))

resp=[]
for letra in let_or:
    inic = [letra]
    count = 0
    for line in a:
        if letra in line:
            count = count + int(line[0])
    inic = inic + [count]
    resp = resp + [inic]
for line in resp:
    print(str(line[0])+","+str(line[1]))