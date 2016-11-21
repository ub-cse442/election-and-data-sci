import csv

k = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
'Virginia', 'Washington', 'West Virginia','Wisconsin', 'Wyoming'
]


years = ['2016','2012', '2008', '2004', '2000']


for year in years:
	csv_file = year + ".csv"
	dataFile = open(csv_file, "r")
	dataFile.readline()

	c = 0
	write_all = [['State', 'Abbreviation','Democratic','Republican']]
	for line in dataFile.readlines():
		data = line.split(",")
		new_data = [ data[0], data[1], data[2][:-2] ]
		state = [k[c]]
		state.extend(new_data)
		write_all.append( state)
		c += 1

	with open( year+".csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(write_all)
	write_all = []




#
