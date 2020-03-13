
def getPos (n_rows, n_cols, row, col) :
    return n_cols*(row-1)+col
def getTrajectorySerpentine (n_rows, n_cols, row, col, i_dir) :
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
def getTrajectoryCircular (n_rows,n_cols,row,col,i_dir) :  
    act_col=col
    act_row=row
    output=''
    circular_val = 0
    done_first = 0
    if i_dir == 'O' or i_dir =='W':
        inicial_row=act_row
        printed_rows=0
        if i_col==1 :
            col_avance=1
        else :
            col_avance=-1
        while 1 :
            output += str(getPos(n_cols,n_rows,act_col, act_row)) + ' '
            #print ('row: '+str(act_row)+'col: ' + str(act_col))
            if (act_col==n_cols and col_avance==1) or (act_col==1 and  col_avance==-1) :
                printed_rows+=1
                if done_first == 0 and inicial_row==1:
                    if printed_rows>=n_rows :
                        return output
                    act_row=n_rows-circular_val
                    done_first=1
                elif done_first!=0 and inicial_row==1 :
                    if printed_rows>=n_rows :
                        return output
                    circular_val+=1
                    act_row=circular_val+1
                    done_first=0
                elif done_first==0 and inicial_row!=1 :
                    if printed_rows>=n_rows :
                        return output
                    act_row=circular_val+1
                    done_first=1
                elif done_first!=0 and inicial_row!=1:
                    if printed_rows>=n_rows :
                        return output
                    act_row=n_cols-circular_val
                    circular_val+=1
                    done_first=0
                col_avance=-col_avance
            else:
                act_col+=col_avance
    elif i_dir == 'N' or i_dir =='S':
        inicial_col=act_col
        printed_cols=0
        if i_row==1 :
            row_avance=1
        else :
            row_avance=-1
        while 1 :
            output += str(getPos(n_rows,n_cols,act_row, act_col)) + ' '
            #print ('col: '+str(act_col)+'row: ' + str(act_row))
            if (act_row==n_rows and row_avance==1) or (act_row==1 and  row_avance==-1) :
                printed_cols+=1
                if done_first == 0 and inicial_col==1:
                    if printed_cols>=n_cols :
                        return output
                    act_col=n_cols-circular_val
                    done_first=1
                elif done_first!=0 and inicial_col==1 :
                    if printed_cols>=n_cols :
                        return output
                    circular_val+=1
                    act_col=circular_val+1
                    done_first=0
                elif done_first==0 and inicial_col!=1 :
                    if printed_cols>=n_cols :
                        return output
                    act_col=circular_val+1
                    done_first=1
                elif done_first!=0 and inicial_col!=1:
                    if printed_cols>=n_cols :
                        return output
                    act_col=n_rows-circular_val
                    circular_val+=1
                    done_first=0
                row_avance=-row_avance
            else:
                act_row+=row_avance
    return output

input = '23 12 23 1 N Z'
splited=input.split()
n_rows=int(splited[0])
n_cols=int(splited[1])
i_row=int(splited[2])
i_col=int(splited[3])
i_dir = splited[4]
tipo=splited[5]
if tipo == 'Z':
    print (getTrajectoryCircular(n_rows,n_cols,i_row,i_col,i_dir))
elif tipo == 'S':
    print (getTrajectorySerpentine(n_rows,n_cols,i_row,i_col,i_dir))
#print(getTrajectory(n_rows,n_cols,i_row,i_col,i_dir))s