from random import shuffle

if __name__ == '__main__':
    formula = []
    start1, end1 = 11, 20
    start2, end2 = 1, 20
    colum = end2 - start2
    row = end1 - start1
    row, colum = colum, row

    for i in range(start1, end1) :
	for j in range(start2, end2) :
	    formula.append((i,j)) 

    shuffle(formula)

    file = open('formula.csv', 'w')

    for k in range(0, row):
	r = formula[k * colum : (k+1)*colum]
	line = ",".join([ '%dX%d=  ' % (i,j) for (i,j) in r])
	print line
	file.write(line+'\n')

    file.close()

