import csv
import pandas as pd
import os


def readColumn(csv_file, col):
    df = pd.read_csv(csv_file)
    column = df[col]
    columns = []
    for each in column:
        columns.append(each)

    #return in a list
    return columns


def checkError( file1 , inp1, type1 ):


    if ( os.path.isfile( file1 ) == False ):
        return "the file does not exist in the directory"

    if (file1[-4:] != '.csv'):
        return "this file is not a csv file"

    else:
        if (type1 == 'row'):
            #inp1 -> two elements ( start and end ) in a list
            dataFile = open(file1, "r")
            first_row = dataFile.readline()
            elements = first_row.split(',')
            for each in inp1:
                if each not in elements:
                    error_message = each + " does not exist in the row "
                    return error_message
        else:
            # column
            #inp1 -> three elements ( column, start, end) in a list
            df = pd.read_csv(file1)
            col = inp1[0]
            column = df[col]
            columns = readColumn(file1, column)
            start = inp1[1]
            end = inp1[2]

            if (start not in columns):
                return start + " does not exist in " + col + " column "
            if (end not in columns):
                return end + " does not exist in " + col + " column "
        print "everything fine:)"


print checkError('total_revised.csv', ['State', 'Georgia', 'Michigan' ] , 'col')

#quit()



def columnRange(csv_file, col, start, stop ):
    columns = readColumn(csv_file, col)
    index1 = columns.index(start)
    index2 = columns.index(stop) + 1
    ranged_columns = columns[index1 : index2]
    return ranged_columns



#
