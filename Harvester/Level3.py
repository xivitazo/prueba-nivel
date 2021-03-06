
def getPos (n_rows, n_cols, row, col) :
    return n_cols*(row-1)+col
def getTrajectory (n_rows, n_cols, row, col, i_dir) :
    act_col=col
    act_row=row
    output=''
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
    if i_dir == 'O' or i_dir =='W':
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

        while 1 :
            #print ('col: '+str(act_col)+'row: ' + str(act_row))
            if (act_col == n_cols and col_avance==1 and act_row==n_rows and row_avance==1) or (act_col==1 and  col_avance==-1 and act_row==n_rows and row_avance==1) or (act_col == n_cols and col_avance==1 and act_row==1 and row_avance==-1) or (act_col==1 and  col_avance==-1 and act_row==1 and row_avance==-1):
                break
            elif (act_col==n_cols and col_avance==1) or (act_col==1 and  col_avance==-1) :
                act_row+=row_avance
                col_avance=-col_avance
            else:
                act_col+=col_avance
            output += str(getPos(n_rows,n_cols,act_row, act_col)) + ' '
    elif i_dir == 'N' or i_dir =='S':
        while 1 :
            output += str(getPos(n_rows,n_cols,act_row, act_col)) + ' '
            #print ('col: '+str(act_col)+'row: ' + str(act_row))
            if (act_col == n_cols and col_avance==1 and act_row==n_rows and row_avance==1) or (act_col==1 and  col_avance==-1 and act_row==n_rows and row_avance==1) or (act_col == n_cols and col_avance==1 and act_row==1 and row_avance==-1) or (act_col==1 and  col_avance==-1 and act_row==1 and row_avance==-1):
                col_avance=-col_avance_0
                row_avance=-row_avance_0
                act_row=i_row
                act_col=i_col
                break
            elif (act_row==n_rows and row_avance==1) or (act_row==1 and  row_avance==-1) :
                act_col+=col_avance
                row_avance=-row_avance
            else:
                act_row+=row_avance

        while 1 :
            #print ('col: '+str(act_col)+'row: ' + str(act_row))
            if (act_col == n_cols and col_avance==1 and act_row==n_rows and row_avance==1) or (act_col==1 and  col_avance==-1 and act_row==n_rows and row_avance==1) or (act_col == n_cols and col_avance==1 and act_row==1 and row_avance==-1) or (act_col==1 and  col_avance==-1 and act_row==1 and row_avance==-1):
                break
            elif (act_col==n_cols and col_avance==1) or (act_col==1 and  col_avance==-1) :
                act_col+=col_avance
                row_avance=-row_avance
            else:
                act_row+=row_avance
            output += str(getPos(n_rows,n_cols,act_row, act_col)) + ' '
    return output
input = '23 12 23 1 N'
splited=input.split()
n_rows=int(splited[0])
n_cols=int(splited[1])
i_row=int(splited[2])
i_col=int(splited[3])
i_dir = splited[4]

print(getTrajectory(n_rows,n_cols,i_row,i_col,i_dir))