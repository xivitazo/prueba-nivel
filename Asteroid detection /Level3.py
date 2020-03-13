def compareShapes (shape1, shape2):
    if (len(shape1)!=len(shape2)):
        return False
    for n in range(len(shape2)):
        if len(shape1[n])!=len(shape2[n]) :
            return False
        for i in range (len(shape2[n])):
           if (shape2[n][i]<=0 and shape1[n][i]>0) or (shape2[n][i]>0 and shape[n][i]<= 0):
               return False
    return True


class Asteroid :
    def __init__(self, shape, timestamp, obs_period) :
        self.inicialTimeStamp=obs_period[0]
        self.finalTimeStamp=obs_period[1]
        self.shape=[]
        self.shape=shape
        self.times=[]
        self.times.append(timestamp)
    
    def posibleSame (self, shape, timestamp) :
        if compareShapes(self.shape,shape) == False :
            return False
        if self.inicialTimeStamp <=timestamp and timestamp <= self.finalTimeStamp :
            self.times.append(timestamp)
            return True
        return False

    def getInfo (self):
        subsets =[]
        output =''
        for n in range(len(self.times)):
            for i in range (len(self.times)) :
                if n == i:
                    continue
                timeDif= self.times[i]-self.times[n]
                if timeDif<0 :
                    continue
                same=0
                for m in subsets:
                    if m[1]%timeDif == 0 or timeDif%m[1]:
                        same=1
                if same == 1:
                    continue
                done=0
                for k in subsets :
                    if k[1]==timeDif :
                        done = 1
                if done == 1: 
                    continue
                subsetInputs =0
                for j in self.times:
                    if j == (self.times[n]-timeDif):
                        subsetInputs+=1
                    elif j== (self.times[n] + 2*timeDif) :
                        subsetInputs+=1
                if subsetInputs == 2 :
                    subset=[]
                    for j in self.times:
                        if abs(self.times[n]-j)%timeDif == 0:
                            subset.append(j)
                    if (min(subset)-timeDif) > 0 and (max(subset)+timeDif) < self.finalTimeStamp :
                        continue
                    same=0
                    for l in subsets:
                        if l[1]%timeDif == 0 or l[0]==min(subset) :
                            same=1
                    if same == 1 :
                        continue
                    subsets.append([min(subset), timeDif])
        
        for n in subsets :
            output_subset=[]
            for i in self.times:
                if (i-n[0])%n[1] == 0 :
                    output_subset.append(i)
            output += str(min(output_subset)) + ' '+ str(max(output_subset)) + ' '+ str(len(output_subset))+ '\n'
        return output




Asteroids= []
input=open("level3_inputs/lvl3-1.inp",'r')
output=open('output.txt', 'w')
actual_line=0
s_input=input.read()
lines=s_input.splitlines()
splited=lines[actual_line].split()
actual_line+=1
start = int(splited[0])
end=int(splited[1])
obs_period=[start,end]
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
            Asteroids.append(Asteroid(shape, timestamp, obs_period))

for n in Asteroids :
    output.write (n.getInfo())

