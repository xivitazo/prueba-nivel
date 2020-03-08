in_file = open ("level1/level1-3.in","r")
out_file = open ("output.txt","w")
splited = in_file.read().split()
rows = int(splited[0])
cols = int (splited[1])
n_pos= int(splited[2])
for n in range (3,n_pos+3,1) :
    pos=int(splited[n])
    col= (pos%cols)
    if col == 0 :
        col = cols
        row=pos/cols
        out_file.write (str (row) + ' '+ str(col)+' ')
        continue
    row= ((pos-(pos%cols))/cols)+1
    out_file.write (str (row) + ' '+ str(col)+' ')