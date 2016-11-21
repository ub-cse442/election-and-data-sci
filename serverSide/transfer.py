#!/usr/bin/python


aList = []
f = open('twitterStreamData.txt','r')     # This is a big file
for line in f:                # Using 'for ... in' on file object
    print line                # ',' keeps print from adding a line break

f.close()

