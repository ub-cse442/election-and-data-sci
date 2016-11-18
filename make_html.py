
from integrate_html import*
#importing integrate_html.py file

import csv
import codecs
import re


def parseCSV_getData ( file1 ): #total.csv

    data = open(file1, "r")
    data.readline()
    data.readline()

    state_map = {}
    for line in data.readlines():
        split = line.split(',')
        state_fullname = split[0]
        state = split[1]

        state_data = []
        state_data.append(state_fullname)

        year = 2000
        for i in range(2,10,2):

            data_year = []
            data_year.append(year)
            D = split[i]; R = split[i+1]
            if i == 8:
                R = R[:-2]
            data_year.append(D)
            data_year.append(R)
            year += 4
            state_data.append(data_year)

        state_map[state] = state_data

    return state_map

#testing
#map1 = parseCSV_getData("total.csv")
#k = map1['AL']
#print k
# output: ['Alabama', [2000, '692611', '941173'], [2004, '693933', '1176394'],
#         [2008, '813479', '1266546'], [2012, '795696', '1255925']]

#quit()
def make_poll_data(state_abb):

    line1 = '<font color ="black"><h2>Data for ' + state_fullname + ' </h2></font>'




def split_make_file(file1):
    f=codecs.open(file1, 'r')
    html_data = f.read()
    parsing_line = '<!--For Parsing-->'


def makeHTML(html_data, make_file):
    Html_file = open(make_file,"w") #make_file = e.g. "WY.html"
    Html_file.write(html_data)
    Html_file.close()




split_make_file("state_temp.html")
