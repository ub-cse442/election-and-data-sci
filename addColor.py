from integrate_html import*
import csv
import re


red_thick = '"#ff3333"'
red_mid = '"#ff8080"'
red_thin = '"#ffb3b3"'
red_skinny = '"#ffe6e6"'


blue_thick = '"#3333ff"'
blue_mid = '"#1aa3ff"'
blue_thin = '"#99d6ff"'
blue_skinny = '"#e6e6ff"'


def give_color(percent):
    if percent > 0.54:
        return blue_thick
    elif (0.54 >= percent > 0.52):
        return blue_mid
    elif (0.52>= percent > 0.505):
        return blue_thin
    elif (0.505>= percent > 0.5):
        return blue_skinny
    elif (0.5>= percent > 0.495):
        return red_skinny
    elif (0.495>= percent > 0.48):
        return red_thin
    elif (0.48>= percent > 0.46):
        return red_mid
    else:
        return red_thick


def color_percent( D, R):
    D = float(D); R = float(R)
    return D/(D + R)


csv_files = ['2000', '2004', '2008', '2012', '2016']




def change_hexColor (line, hex_color):
    reg_color = 'fill="#[0-9a-fA-F]{6}"'
    get_color = re.findall(reg_color, line)

    new_line = line.split(get_color[0])[0] + 'fill=' + hex_color + line.split(get_color[0])[1]
    return new_line


def combine_lines(states, state_html, state_color):

    lines = []
    for state in states:
        if 'data-info' in state:
            first = getHead(state)
            state_abb = getState(state)
            middle = state_html[state_abb]
            end = getAfterFill(state)
            line = first + middle + end

            hex_color = state_color[state_abb]
            new_line = change_hexColor( line, hex_color)
            lines.append(new_line)
    return lines



def make_line( state_fullname, D, R, year):

    html_line = '<div> <p> <h4>' + state_fullname + '</h4> </p></div> <div><p>' + space18 + 'Demo ' + space + space + space + 'Repub' + space4 + '</p></div> '

    a1, a2, b1, b2 = makeBolds(D, R)
    D_comma = addComma(D); R_comma = addComma(R)
    temp = '<div>' + year + ' : ' + a1 + D_comma + a2 + space + b1 + R_comma + b2 + '</div>'
    html_line += temp

    return html_line


def html_lines(file1):
    #return <path id = ..> #total 50 lines
    f=codecs.open(file1, 'r')
    html_data = f.read()
    state_before = '<g id="outlines">'
    state_after = '</g>'

    first = html_data.split(state_before)[0]
    end = html_data.split(state_after)[1]

    states = html_data.split(state_before)[1].split(state_after)[0]
    reg1 = '<path id=.+?. fill=.+?."/>'
    states_reg = re.findall(reg1, states)
    return states_reg, [first , state_before, state_after, end]




def html_allLines( all_lines, rest):
    first = rest[0]; state_before = rest[1]; state_after = rest[2]; end = rest[3]
    middle = "\n"
    for line in all_lines:
        middle += '  ' + line + '\n'
    middle += '  <path id="DC" fill="#D3D3D3" stroke="#FFFFFF" stroke-width="1.5" cx="801.3" cy="251.8" r="5"/>' + '\n'

    return first + state_before +  middle + state_after + end


def main(files, data_file):

    for file1 in files:
        year = file1
        file1 += '.csv'
        data = open(file1, "r")
        data.readline()
        state_html = {}
        state_color = {}
        percent = []
        for line in data.readlines():
            split = line.split(',')
            state_fullname = split[0]
            state_abb = split[1]
            D = split[2]
            R = split[3][:-2]

            state_color[state_abb] = give_color( color_percent(D,R) )
            percent.append(color_percent(D,R))
            state_html[state_abb] = make_line(state_fullname, D, R, year)

        core_lines, rest = html_lines(data_file)
        all_lines = combine_lines( core_lines, state_html , state_color)


        total_lines = html_allLines( all_lines , rest)

        new_file = 'data_' + year + '.html'
        makeHTML(new_file, total_lines)



main(csv_files, "data.html")



#
