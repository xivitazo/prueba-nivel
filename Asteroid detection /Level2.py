class Asteroid :
    def __init__(self, shape, timestamp) :
        self.shape=[]
        self.shape=shape
        self.times=[]
        self.times.append(timestamp)
    
    def posibleSame (self, shape, timestamp) :
        if (len(shape)!=len(self.shape)):
            return False
        for n in range(len(self.shape)):
            if len(shape[n])!=len(self.shape[n]) :
                return False
            for i in range (len(self.shape[n])):
                if (self.shape[n][i]<=0 and shape[n][i]>0) or (self.shape[n][i]>0 and shape[n][i]<= 0):
                    return False
        self.times.append(timestamp)
        return True

    def getInfo (self):
        return str(self.times[0]) +' '+ str(self.times[-1]) + ' ' + str(len(self.times))




Asteroids= []
input=open("level2_inputs/lvl2-4.inp",'r')
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
    min_row=rows
    max_row=0
    min_col=cols
    max_col=0

    for i in range(rows) :
        for j in range(cols) :
            if image [i][j] > 0 :
                if i>0 :
                    if image [i-1][j]>0 :
                        if i-1 < min_row:
                            min_row=i-1
                        if i > max_row :
                            max_row=i
                        printable=1
                if j>0 :
                    if image [i][j-1]>0 :
                        if j-1 < min_col:
                            min_col=j-1
                        if j > max_col :
                            max_col=j
                        printable=1
    if printable == 1:
        shape=[]
        for i in range (min_row, max_row+1,1):
            row=[]
            for j in range(min_col,max_col+1,1):
                row.append(image[i][j])
            shape.append(row)

        found=0
        for n in Asteroids :
            if n.posibleSame(shape, timestamp) == True :
                found=1
                break
        if found==0 :
            Asteroids.append(Asteroid(shape, timestamp))

for n in Asteroids :
    output.write (n.getInfo() + '\n')

