import csv

years = ['2012', '2008', '2004', '2000']

def writeToCSV ( years ):

    years = sorted(years)
    DR = ['Democratic', 'Republican']
    for i in range( len(years) / 2  + 1 ):
        DR.append( DR[0] )
        DR.append( DR[1] )
    header = [ "State", "Abbreviation" ]
    header.extend( DR )


    file_2000 = "2000.csv"
    file_2004 = "2004.csv"
    file_2008 = "2008.csv"
    file_2012 = "2012.csv"

    data_2000 = open(file_2000, "r")
    data_2004 = open(file_2004, "r")
    data_2008 = open(file_2008, "r")
    data_2012 = open(file_2012, "r")

    data_2000.readline()
    data_2004.readline()
    data_2008.readline()
    data_2012.readline()

    write_all = [ header ]
    for i in range(51):
        line1 = data_2000.readline()
        line2 = data_2004.readline()
        line3 = data_2008.readline()
        line4 = data_2012.readline()

        data1 = line1.split(",")
        data2 = line2.split(",")
        data3 = line3.split(",")
        data4 = line4.split(",")

        new_list = [ data1[0], data1[1], data1[2], data1[3][:-2], data2[2], data2[3][:-2],
                     data3[2], data3[3][:-2], data4[2], data4[3][:-2] ]
        write_all.append( new_list )
    with open( "total.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(write_all)


writeToCSV(years)




#
