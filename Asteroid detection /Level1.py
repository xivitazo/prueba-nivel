input=open("lvl1-4.inp",'r')
output=open('output.txt', 'w')
actual_line=0
s_input=input.read()
lines=s_input.splitlines()
splited=lines[actual_line].split()
actual_line+=1
start = int(splited[0])
end=int(splited[1])
n_images=int(splited[2])
for n in range(n_images) :
    image = []
    splited=lines[actual_line].split()
    actual_line+=1
    timestamp=int(splited[0])
    rows=int(splited[1])
    cols=int(splited[2])
    for i in range(rows):
        row=lines[actual_line].split()
        actual_line+=1
        int_row=[]
        for j in range (cols):
            int_row.append(int(row[j]))
        image.append(int_row)
    printable=0
    for i in range(rows) :
        for j in range(cols) :
            if image [i][j] > 0 :
                if i>1 :
                    if image [i-1][j]>0 :
                        printable=1
                if j>1 :
                    if image [i][j-1]>0 :
                        printable=1
    if printable == 1:
        output.write(str(timestamp) + '\n')



