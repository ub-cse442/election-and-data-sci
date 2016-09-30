import matplotlib.pyplot as plt
import pandas
import csv


with open('2004.csv', newline='') as csvfile:

    statelist=[]
    republicanlist =[]
    democratlist=[]
    filereader = csv.reader(csvfile, delimiter=',')

    for line in filereader:


        statelist.append(line[0])
        democratlist.append(line[1])
        republicanlist.append(line[2])


del(statelist[0],democratlist[0],republicanlist[0])

plt.figure(1)
x = range(len(statelist))
plt.xticks(x, statelist)
plt.plot(x,democratlist,"b")
plt.plot(x,republicanlist,"r")
plt.xticks(range(0,len(statelist)))
plt.show()

