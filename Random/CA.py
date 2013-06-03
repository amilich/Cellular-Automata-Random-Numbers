import time

class CAGen(object):
    """This class contains and supports the CA generation"""
    array = [] #contains the CA
    def __init__(self, n=5, prevData = False, prevStr = ""):
        self.n = n
        self.array = [[0]*n for x in range(n)]
        if not prevData: 
            self.array[0][int(n/2)] = 1
        else:
            for i in range(len(prevStr)):
                self.array[0][i] = int(prevStr[i])
        array = self.array
        self.next = 1
                
    def __repr__(self):
        """this runs if you print the CA; it shows nVal"""
        return "This is a CA; n = %d." %self.n #essentially the toString() function
    
    def printArray(self):
        """prints entire array"""
        for x in range(len(self.array)):
            print self.array[x]

    def loop(self, steps=1):
        """loops array to compute 0's and 1's"""
        [self.step() for i in range(steps)]

    def step(self):
        """computes next val for a cell in the array"""
        array = self.array

        i = self.next
        for j in range(len(array[0])):
            if j > 0 and j < len(array[0])-1:
                nextNum = self.computeNext(array[i-1][j-1], array[i-1][j],array[i-1][j+1])
                if nextNum == 1:
                    array[i][j] = 5

        for jj in range(len(array[0])):
                    if array[self.next][jj] == 5:
                            array[self.next][jj] = 1

        if(self.next < len(array)):
            self.next += 1

    def getColumnDec(self):
        """grabs the center column; converts 0's and 1's to decimal representation"""
        num = 0
        for i in range(len(self.array)):
            currentNum = self.array[i][int(len(self.array[0])/2)]*(2**i)
            num += currentNum
        return num

    def getRowBin(self):
        """grabs last row in binary - used to save seed"""
        num = ""
        for i in range(len(self.array[0])):
            currentNum = self.array[len(self.array)-1][i]
            num += str(currentNum)
        return num

    def getColumnBin(self):
        """gets center column in binary"""
        num = ""
        for i in range(len(self.array)):
            currentNum = self.array[i][int(len(self.array[0])/2)]
            num += str(currentNum)
        return num
        
    def computeNext(self, aboveLeft, aboveCen, aboveRight):
        """rules for computing next seed"""
        if aboveLeft == 1 and aboveCen == 1 and aboveRight == 1:
            return 0
        if aboveLeft == 1 and aboveCen == 1 and aboveRight == 0:
            return 0
        if aboveLeft == 1 and aboveCen == 0 and aboveRight == 1:
            return 0
        if aboveLeft == 1 and aboveCen == 0 and aboveRight == 0:
            return 1
        if aboveLeft == 0 and aboveCen == 1 and aboveRight == 1:
            return 1
        if aboveLeft == 0 and aboveCen == 1 and aboveRight == 0:
            return 1
        if aboveLeft == 0 and aboveCen == 0 and aboveRight == 1:
            return 1
        if aboveLeft == 0 and aboveCen == 0 and aboveRight == 0:
            return 0
        else:
            return 0
            

def getFileData(myFile): 
    """checks if there is seed data"""
    a = myFile.readline()
    for line in myFile:
        if "*" in line:
            #print 'no data: ' + line
            return ""
    myFile.close()
    return a

def writeFileData(myFile, a, record=False):
    """writes seed to file"""
    #print 'written' + str(a.getColumnBin())
    myFile.truncate()
    myFile.write(a.getColumnBin())
    if record:
        seedFile = open('seeds.txt', 'r')
        lines = seedFile.readlines()
        seedFile.close()
        seedFile = open('seeds.txt', 'w')
        if(len(lines) < 500):
            seedFile.writelines(a.getColumnBin() + '\n')
        seedFile.writelines(lines)

def toBase10(x):
    """converts given integer - x - to base 10"""
    return int(x, 2)


