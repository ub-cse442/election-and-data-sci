import matplotlib.pyplot as plt
import pandas
import csv
import numpy as np

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

    pos = range(0,len(statelist))
    x = range(len(statelist))

    width = 0.25

    plt.xticks(x, statelist)
    plt.bar(x,democratlist,width,alpha=0.5,color='blue',label = 'Democrat')
    plt.bar([p + width for p in pos],republicanlist,width,alpha=0.5,color='red',label='Republican')
    plt.xticks(range(0, len(statelist)))
    plt.ylabel('No of votes')
    plt.xlabel('States')
    plt.title('Democrat Vs Republican')
    plt.legend(['Democrat', 'Republican'], loc='upper right')
    plt.grid()
    plt.savefig('rep_vs_dem_bar_2012.png')

    plt.show()












if __name__=="__main__":
    sun_data('2012.csv')