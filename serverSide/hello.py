#!/usr/bin/python


file = open("/usr/local/apache2/cgi-bin/text.txt", "r")

items = file.readline().split()


print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title> Live Stream</title>'
print '</head>'
print '<body background ="http://www.pptgrounds.com/wp-content/uploads/2012/12/American-Patriotic-Flag-PPT-Backgrounds-1024x768.jpg">'
print ' <center><strong><font size="7">DONALD TRUMP LIVE SENTIMENT</font></strong></center> </div>'
str.center(10,items)
print '</body>'
print '</html>'

