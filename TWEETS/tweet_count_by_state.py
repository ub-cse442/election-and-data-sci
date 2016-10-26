import csv

with open('Hillary1.csv',encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if('fuck you6' in row[0]):
            print(row[0])

