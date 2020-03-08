input = "23 12"
def getPos (n_rows, n_cols, row, col) :
    return n_cols*(row-1)+col
splited = input.split()
n_rows=int(splited[0])
n_colums=int(splited[1])
act_row=1
act_col=1
avance=1
output=''
while 1 :
    output += str(getPos(n_rows,n_colums,act_row, act_col)) + ' '
    #print ('col: '+str(act_col)+'row: ' + str(act_row))
    if (act_col == n_colums and avance==1 and act_row==n_rows) or (act_col==0 and  avance==-1 and act_row==n_rows) :
        break
    elif (act_col==n_colums and avance==1) or (act_col==1 and  avance==-1) :
        act_row+=1
        avance=-avance
    else:
        act_col+=avance
print(output)