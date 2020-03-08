input = "23 12"
def getPos (n_rows, n_cols, row, col) :
    return n_cols*(row)+col
splited = input.split()
n_rows=int(splited[0])
n_colums=int(splited[1])
avance=-1
output=''
for i in range(n_rows) :
    avance=-avance
    for n in range(n_colums) :
        if avance == 1:
            #print ('imprimiendo al derecho')
            output += str(getPos(n_rows,n_colums, i, n+1)) + ' '
        else :
            #print ('imprimiendo al reves')
            output += str(getPos(n_rows,n_colums, i, n_colums-n)) + ' '
print(output)