####
#still working on this.
####
import csv
import codecs
import re



state_before = '<g id="outlines">'
state_after = '</g>'




space4 = '&nbsp;&nbsp;&nbsp;&nbsp;'
space6 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
space18 = space6 + space6 + space6


def makeBolds(num1, num2):
    n1, n2 = noComma(num1), noComma(num2)
    a1 = ''; a2 = ''; b1 = ''; b2 = ''
    if n1 > n2:
        a1 = '<b>'
        a2 = '</b>'
    else n1 > n2:
        b1 = '<b>'
        b2 = '</b>'
    return a1, a2 , b1, b2


str1 = '<path id="CO" data-info="<div>Colorado</div><div>9 electoral votes</div>" fill="#89CFF0" d="M378.6,256.8l1.4-21.3l-32.1-3.1l-24.5-2.7l-37.3-4.1l-20.7-2.5l-2.6,22.2l-3.2,22.4l-3.8,28 l-1.5,11.1l-0.3,2.8l33.9,3.8l37.7,4.3l32,3.2l16.6,0.8"/>'


#str1 = '<path id="AK" data-info="<div> <b>This is some text!<.6,0.8"/>'
def getLine(lines):


    re1 = '<path id=".+?." data-info='
    re2 = 'fill'
    re3 = '"/>'
    myre = re1 + '(.+?)' +re2 + '(.+?)' + re3

    return re.findall(myre, lines)

print getLine(str1)

quit()

#<font color ="blue">A table of the US past president election polls</font>

f=codecs.open("data3.html", 'r')
html_data = f.read()


Html_file = open("temp.html","w")
Html_file.write(html_data)
Html_file.close()



quit()
def addComma ( num ):
    num = str(num)
    num_len = len(num)

    new_num = ""
    c = 0
    for i in reversed(range(num_len)):
        new_num = num[i] + new_num
        c += 1
        if c==3 and i != 0:
            new_num = ',' + new_num
            c = 0
    return new_num



def readHTML ():
    f=codecs.open("data3.html", 'r')
    html_data = f.read()

    reg1 = '<path id=.+?. fill='
    states = re.findall(reg1, html_data)
    return states


def parseCSV ( file1 ):

    data = open(file1, "r")
    data.readline()
    data.readline()

    # 2 ~ 9
    state_map = {}
    for line in data.readlines():
        split = line.split(',')
        state_fullname = split[0]
        state = split[1]
        html_line = '<div>2000 : ' + addComma(split[2]) + ' ' + addComma(split[3]) + '</div>'
        html_line += '<div>2004 : ' + addComma(split[4]) + ' ' + addComma(split[5]) + '</div>'
        html_line += '<div>2008 : ' + addComma(split[6]) + ' ' + addComma(split[7]) + '</div>'
        html_line += '<div>2012 : ' + addComma(split[8]) + ' ' + addComma(split[9][:-2]) + '</div>" fill='
        state_map[state] = [state_fullname, html_line]

    return state_map

state_map = parseCSV('total.csv')
states = readHTML()
reg_state = '".+?."'
state_abb = re.findall( reg_state, states[0] )[0][1:-1]

html_line, state_fullname = (state_map [ state_abb ])[0], (state_map [ state_abb ])[1]
print html_line
print state_fullname
quit()



line1 = '<path id="' # + state_abb AK
line2 = '" data-info="<div> <p> <h4> ' #+ state  Alaska
line3 = ' </h4> </p> </div> <div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Demo &nbsp;&nbsp;&nbsp;Repub</p></div> '
#line4 = html_line
print states[0]
quit()
nbsp1 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
nbsp2 = '&nbsp;&nbsp;&nbsp;'
k = '<path id="AK" data-info="<div> <p> <h4> Alaska </h4> </p> </div> <div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Demo &nbsp;&nbsp;&nbsp;Repub</p></div> <div>2000 : 143,312 164,324</div><div>2004 : 143,762 198,324</div><div>2008 : 523,312 754,324</div>" fill='


#parseCSV( 'total.csv' )





#
