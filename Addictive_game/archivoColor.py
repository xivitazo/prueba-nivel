class Color :
    def __init__(self, rows, cols):
        #super().__init__()
        self.rows=rows
        self.cols=cols
        self.points = []
    def addPoint (self,pos):
        self.col= (pos%self.cols)
        if self.col == 0 :
            self.col = self.cols
            self.row=pos/self.cols
            self.points.append([self.row,self.col])
            del self.col
            del self.row
            return
            #out_file.write (str (row) + ' '+ str(col)+' ')
        self.row= ((pos-(pos%self.cols))/self.cols)+1
        self.points.append([self.row,self.col])
        del self.col
        del self.row
        #out_file.write (str (row) + ' '+ str(col)+' ')

    def printPoints (self) :
        for point in self.points :
            print ( 'row :' + str(point[0])+' col: '+ str(point [1]))

    def getMH (self):
        return abs(self.points[0][0] - self.points[1][0])
        
    
    
