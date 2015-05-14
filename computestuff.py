__author__ = 'BisharaKorkor'

import arrayops as ao
from numpy import genfromtxt

data = genfromtxt('ugh.csv', delimiter=',')
n = open('linedata.txt', 'w')
years = [i[2] for i in data]
values = [i[3] for i in data]

for i in range(16):
    y = [years[j+i] for j in range(10)]
    v = [(values[j+i*10]-32)*5/9 for j in range(10)]


    # n.write("[\'" + str(1845 + i*10) + "\', " + str(ao.mean(v)-1.5*ao.stddev(v)) + ", " + str(ao.mean(v)-.1) + ", " +\
    #         str(ao.mean(v)+.1) + ", " + str(ao.mean(v)+1.5*ao.stddev(v)) + "],\n")

    #n.write("[" + str(1845 + i*10) + ", " + str(ao.mean(v)) + ", " + str(ao.mean(v)-2*ao.stddev(v)) + ", " + str(ao.mean(v)+2*ao.stddev(v)) + "],\n")


    n.write()

n.close()