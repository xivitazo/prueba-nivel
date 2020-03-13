input = '5 2 5 2'
def getPos (n_rows, n_cols, row, col) :
    return n_cols*(row-1)+col
splited=input.split()
n_rows=int(splited[0])
n_cols=int(splited[1])
i_row=int(splited[2])
i_col=int(splited[3])

output=''
act_row=i_row
act_col=i_col

if i_col==1 :
    col_avance=1
else :
    col_avance = -1
if i_row==1 :
    row_avance=1
else :
    row_avance=-1
row_avance_0=row_avance
col_avance_0=col_avance
while 1 :
    output += str(getPos(n_rows,n_cols,act_row, act_col)) + ' '
    #print ('col: '+str(act_col)+'row: ' + str(act_row))
    if (act_col == n_cols and col_avance==1 and act_row==n_rows and row_avance==1) or (act_col==1 and  col_avance==-1 and act_row==n_rows and row_avance==1) or (act_col == n_cols and col_avance==1 and act_row==1 and row_avance==-1) or (act_col==1 and  col_avance==-1 and act_row==1 and row_avance==-1):
        col_avance=-col_avance_0
        row_avance=-row_avance_0
        act_row=i_row
        act_col=i_col
        break
    elif (act_col==n_cols and col_avance==1) or (act_col==1 and  col_avance==-1) :
        act_row+=row_avance
        col_avance=-col_avance
    else:
        act_col+=col_avance



print (output)