
#importing integrate_html.py file
from integrate_html import*

import csv
import codecs
import re
import os

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
        for i in range(2,12,2):

            data_year = []
            data_year.append(year)
            D = split[i]; R = split[i+1]
            if i == 10:
                R = R[:-2]
            data_year.append(D)
            data_year.append(R)
            year += 4
            state_data.append(data_year)

        state_map[state] = state_data

    return state_map

#testing
#map1 = parseCSV_getData("total_updated.csv")
#k = map1['AL']
#print k

# output: ['Alabama', [2000, '692611', '941173'], [2004, '693933', '1176394'], [2008, '813479', '1266546'], [2012, '795696', '1255925'], [2016, '718084', '1306925']]


def make_file(first, end, state_abb ):
    state_map = parseCSV_getData("total_updated.csv")
    data = state_map[state_abb]
    state_fullname = data[0]

    l1 = '<font color ="black"><h2>Data for ' + state_fullname + ' </h2></font>'
    l2 = '</br></br>'
    l3 = '<p class="alignright">2016 ' + state_fullname + ' poll results by county</p>'
    l4 = '</br>'
    l5 = '<img\n'; l6 = 'src="' + state_abb.lower() + '.svg"\n' ; l7 = 'height="600px"'
    l8 = 'width="600px"' ; l9 = '/>'
    l10 = '</br></br></br></br>'

    data_size = len(data)
    data_lines = ''
    for i in range(1, data_size):
        each = data[i]
        year = str(each[0]); D = each[1]; R = each[2]
        t1 = '<p class="alignleft">' + year + ':' + space + space
        t1 += D + space4 + R + '</p>\n'
        t2 = '</br></br>\n'
        data_lines += t1 + t2

    all_lines = l1 + l2 + l3 + l4 + l5+ l6 + 'align = "right"\n' + l7 + l8 + l9 + l10 + data_lines
    return all_lines


def split_file(html_file, csv_file):
    f=codecs.open(html_file, 'r')
    html_data = f.read()
    parsing_line = '<!--For Parsing-->'
    parsing_line2 = '<!--Parsing Ends-->'

    first = html_data.split(parsing_line)[0]
    end = html_data.split(parsing_line2)[1]

    data = open(csv_file, "r")
    data.readline()
    data.readline()

    for line in data.readlines():
        split = line.split(',')
        state_abb = split[1]
        lines = make_file(first, end, state_abb)
        make_html(first + lines + end, state_abb)


def make_html(html_data, state_abb):
    os.chdir('states')
    Html_file = open( state_abb + ".html" ,"w") #make_file = e.g. "WY.html"
    Html_file.write(html_data)
    Html_file.close()
    os.chdir('..')


split_file("state_temp.html", "total_updated.csv")


#
