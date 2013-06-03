import time
from CA import *
import os

minRands = 100 #minimum number of randoms in the file
curpath = os.path.abspath(os.curdir) 
rand_file = "%s" % ("rands.txt") #name of file with randoms
init_file = "%s" % ("init.txt") #name of file with last seed
dictionary = {}

def initCA(nVal,printN=False):
    """initiates the CA with a given n value - the size of the array is nxn"""
    initData = openFile()
    if(len(initData) > 0) and not "*" in initData:
        n = len(initData)
        if printN:
            print "N = " + str(n)
        a = CAGen(nVal, True, initData)
    else:
        a = CAGen(nVal, False)
    return a

def init():
    """sets directory to open file"""    
    os.chdir(r"/Library/Python/2.7/site-packages/rand_mod")
    return

def openFile():
    """opens init file for reading, returns data from file"""
    myFile = open(init_file, 'r+')
    return getFileData(myFile)

def closeFile(a):
    """closes init file; writes new seed"""
    #myFile = open('init.txt', 'w')
    myFile = open(init_file, 'w')
    writeFileData(myFile, a)

def getRandFloat(a):
    """gets the number from the center column in the file; scales it from 0 to 2^n"""
    rand = a.getColumnDec()
    rand = float( float(rand)/( float(2**(a.n)-1) ) )
    return rand

def manageCA(a):
    """loops the CA to fill it with 0's and 1's"""
    a.loop(a.n-1)
    #a.loop(a.n/2)
    closeFile(a)
    nUsed = a.n

def createValDict(a, precision=1):
    d = {}
    val = round(getRandFloat(a), precision)
    if val in d.keys():
        d[val] += 1
    else:
        d[val] = 1
    return d

def _fileUpkeep(minNum=1000,nVal=25):
    """keeps dictionary of different randoms and their frequency; returns a dict"""
    #myFile = open('rands.txt', 'r+')
    myFile = open(rand_file, 'r+')
    fileLength = 0
    for line in myFile:
        fileLength += 1
    if fileLength < minNum:
        a = initCA(nVal,False)
        for x in range(minRands):
            a = initCA(nVal,False)
            manageCA(a)
            #d = createValDict(a,d)
            myFile.write(str(getRandFloat(a))+'\n')
            nUsed = nVal

def randFloat(minNum=100,nVal=25):
    """function to use for getting a float - no init conditions needed"""
    init()
    _fileUpkeep(minNum,nVal)
    #myFile = open('rands.txt', "r")
    myFile = open(rand_file, 'r')
    lines = myFile.readlines()
    readFrom = 0
    try:
        if float(lines[0]) > 10**(-5):
            num = float(lines[0])
            readFrom = 1
        else:
            num = float(lines[1])
            readFrom = 2
    except (ValueError):
        num = float(lines[2])
        readFrom = 3
    myFile.close()
    #myFile = open('rands.txt', "w")
    myFile = open(rand_file, 'w')
    myFile.truncate()
    myFile.writelines(lines[readFrom:])
    return num
    
def randInt(low=0,high=2**25):
    """scales integer to given input range"""
    return int(low + (high-low)*randFloat())

def getDict(genVal=100, newFile=False,nVal=25):
    """generates dictionary for graphing"""
    return runGraphGen(genVal,newFile,nVal)

def clearFiles():
    """wipes all files - userful when testing runtime"""
    deleteFile = open('init.txt', 'w')
    deleteFile.write("*")
    deleteFile.close()
    deleteFile = open('rands.txt','w')
    deleteFile.close()
    return

def runGraphGen(genNum,newFile=False,nVal=25):
    """generates randoms for graphing"""
    if newFile:
        clearFiles()
    #genNum = 100
    #print 'Starting time measurement cycle; generating %d randoms.' %genNum

    start = time.clock()
    _fileUpkeep(100,nVal)
    ones = 0
    zeroes = 0
    numList = []
    d = {}
    for x in xrange(genNum):
        if newFile: 
            tempNum = randFloat(100,nVal)
        else:
            tempNum = randFloat(1000)
        #numList.append(tempNum)
        if round(tempNum) == 0:
            zeroes += 1
        else:
            ones += 1

        val = round(tempNum,1)
        if val in d.keys():
            d[val] += 1
        else:
            d[val] = 1
    #this printed the rounded values from 0 to 1
    """for key,val in d.iteritems():
        print key,val
    print "Ones: " + str(ones)
    print "Zeroes: " + str(zeroes)"""
    elapsed = (time.clock() - start)
    #print "Total time was " + str(elapsed) + "."
    if newFile:
        clearFiles()
    return d

def main():
    """nothing should be here"""
    return

if __name__=="__main__":
    main()
