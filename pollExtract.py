import re
import urllib2
import sys
import csv



#check if python version 3.X or 2.X
if (sys.version_info > (3, 0)):
	def myRequest(web):
		return (urllib2.request.urlopen(web)).read()
else:
	def myRequest(web):
		return (urllib2.urlopen(web)).read()

def makeYears ():
	start = 2012
	year_list = []
	# get data from 2012 ~ 1992
	for i in range(4):
		year_list.append(str(start))
		start -= 4
	return year_list



# alphabetically, total 50 States
def getStates ():
	temp_html = myRequest('http://state.1keydata.com/')

	cut1 = '<br><p>Please click on the state you are interested in to view that state\'s information:<br>\n'
	cut2 = '<p>Each page includes the following:'

	re1 = '<a href=".+?..php">'
	re2 = '</a>'
	myre = re1 + '(.+?)' + re2

	return re.findall(myre, temp_html)


def wikiStateData (year):

	html = myRequest('https://en.wikipedia.org/wiki/United_States_presidential_election,_' + year)

	re1 = '<a href="/wiki/United_States_presidential_election_in_.+?." title="United States presidential election in .+?.">.+?.</a></td>'
	states = re.findall(re1, html)

	re2 = '</tr>'

	whole_list = []
	whole_list.append( ['State', 'Democratic', 'Republican'] )
	for state in states:
		temp_html = html.split(state)[1].split(re2)[0]

		td1 = '<td>'
		td2 = '</td>'

		myre = td1 + '(.+?)' + td2

		td_list = re.findall(myre, temp_html)
		state_abbre = td_list[-1]

		demo = td_list[1].replace(',', '')
		repub = td_list[4].replace(',', '')

		data_list = [ state_abbre , demo, repub]
		whole_list.append( data_list )
	return whole_list

def writeCSV ():

	years = makeYears()
	for year in years:
		csv_file = year + '.csv'
		stateList = wikiStateData(year)

		with open(csv_file , "wb") as f:
		    writer = csv.writer(f)
		    writer.writerows(stateList)


writeCSV()




#
