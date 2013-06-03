from __init__ import *
import matplotlib.pyplot as plt
import numpy
from matplotlib.backends.backend_pdf import PdfPages

"""this graphs the distribution of randoms from a given n value (size of CA array)"""

nVal = 42 #the size of the cellular automata
numRow = 3 #the number of graphs to display - 3 is a comfortable fit on the screen
stdDist = [] #holds computed standard deviations
numGen = 3000 #number to generate

for x in range(numRow): #generate the graphs
    d = getDict(numGen,True,nVal) #grabs dictionary from random gen (in myRand.py)
    
    keys = d.keys() #used for numerical sorting
    values = [] #these are used so the data is numerically sorted
    keys.sort()
    myD = {}
    for key in keys:
        values.append(d[key]) 

    for num in range(len(keys)):
        myD.update({keys[num]:values[num]})
    
    plt.figure(1)
    plt.subplot(numRow*100+10+x)
    plt.title("N: " + str(nVal))
    plt.bar(range(len(keys)), values, align = 'center')
    plt.xticks(range(len(keys)), keys)
    myList = []
    for num in xrange(10):
        myList.append(numGen/10)
    plt.plot(xrange(0,10),myList)
    stdDist.append(numpy.std(values)) #gets standard deviation
    nVal -= 2

stdDist.sort()
print stdDist
plt.text(0,0,str(stdDist[0]),fontsize=15)
plt.show()

