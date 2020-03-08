from archivoColor import Color
in_file = open ("level2/level2-1.in","r")
out_file = open ("output.txt","w")
splited = in_file.read().split()
rows = int(splited[0])
cols = int (splited[1])
n_pos= int(splited[2])
colores= []
n_colores = 0
for n in range (3,2*n_pos+3,2) :
    pos=int(splited[n])
    color=int (splited[n+1])
    if color>n_colores :
        colores.append(Color(rows,cols))
        print ("Nuevo color")
        n_colores+=1
    colores[color-1].addPoint(pos)
print (n_colores)
for n in colores :
    out_file.write (str(n.getMH()) + ' ')