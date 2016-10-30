
import csv
import codecs
import re


#global variables
space = '&nbsp;'
space4 = '&nbsp;&nbsp;&nbsp;&nbsp;'
space6 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
space18 = space6 + space6 + space6


def getState(state):
    reg1 = '".+?."'
    state_abb = re.findall(reg1, state)
    return state_abb[0][1:-1]


#state = 'votes</div>" fill="#FA8072" d="M161"/>'
def getAfterFill(state):
    reg1 = '" fill=.+."/>'
    state_rest = re.findall(reg1, state)
    return state_rest[0]

#state1 = '<path id="AK" data-info="<div>" fill ="#afef" />'
def getHead(state):
    reg1 = '<path id=".+." data-info="'
    reg2 = '<path id=".+.".+.data-info="'
    get_front = re.findall(reg1, state)
    get_front2 = re.findall(reg2, state)
    get_front.extend(get_front2)
    return get_front[0]


def makeBolds(n1, n2):
    n1 = int(n1); n2 = int(n2)
    a1 = ''; a2 = ''; b1 = ''; b2 = ''
    if n1 > n2:
        a1 = '<b>'
        a2 = '</b>'
    else:
        b1 = '<b>'
        b2 = '</b>'
    return a1, a2 , b1, b2


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


def parseCSV_line ( file1 ):

    data = open(file1, "r")
    data.readline()
    data.readline()

    # 2 ~ 9
    state_map = {}
    for line in data.readlines():
        split = line.split(',')
        state_fullname = split[0]
        state = split[1]

        year = 2000
        html_line = '<div> <p> <h4>' + state_fullname + '</h4> </p></div> <div><p>' + space18 + 'Demo ' + space + space + space + 'Repub' + space4 + '</p></div> '
        for i in range(2,10,2):
            D = split[i]; R = split[i+1]
            if i == 8:
                R = R[:-2]
            a1, a2, b1, b2 = makeBolds(D, R)
            D_comma = addComma(D); R_comma = addComma(R)
            temp = '<div>' + str(year) + ' : ' + a1 + D_comma + a2 + space + b1 + R_comma + b2 + '</div>'
            html_line += temp
            year += 4

        state_map[state] = html_line

    return state_map


def makeLine(state, state_abb):
    state_hashMap = parseCSV_line( "total.csv")
    info = state_hashMap[state_abb]
    return info


def parseStates(states):

    lines = []
    for state in states:
        if 'data-info' in state:
            first = getHead(state)
            state_abb = getState(state)
            middle = makeLine(state, state_abb)
            end = getAfterFill(state)
            line = first + middle + end
            lines.append(line)
    return lines



def split_make_file():

    f=codecs.open("data.html", 'r')
    html_data = f.read()
    state_before = '<g id="outlines">'
    state_after = '</g>'

    first = html_data.split(state_before)[0]
    end = html_data.split(state_after)[1]

    states = html_data.split(state_before)[1].split(state_after)[0]
    reg1 = '<path id=.+?. fill=.+?."/>'
    states_reg = re.findall(reg1, states)
    #print states_reg
    #quit()
    lines = parseStates(states_reg)
    middle = "\n"

    for line in lines:
        middle += '  ' + line + '\n'
    middle += '  <path id="DC" fill="#D3D3D3" stroke="#FFFFFF" stroke-width="1.5" cx="801.3" cy="251.8" r="5"/>' + '\n'


    return first + state_before +  middle + state_after + end




def makeHTML(html_data):
    Html_file = open("data.html","w")
    Html_file.write(html_data)
    Html_file.close()

makeHTML(split_make_file())

#
