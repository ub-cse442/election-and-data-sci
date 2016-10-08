import matplotlib.pyplot as plt
import pandas
import csv

#author : lethiraj

def sun_data(file):
    with open(file) as csvfile:

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
    plt.plot(x,democratlist,"b",label = 'Democrat')
    plt.plot(x,republicanlist,"r",label = 'Republican')
    plt.xticks(range(0,len(statelist)))
    plt.legend(loc = 'upper right')
    plt.savefig('rep_vs_dem_2008.png')
    plt.show()


if __name__=="__main__":
    sun_data('2008.csv')