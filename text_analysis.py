
from nltk.corpus import inaugural
from numpy import*
from pylab import*

from nltk.book import text4
#count=0
#import nltk
#nltk.download()
#quit()
def getWords():
    for word in text4[0:1000]:
        if len(word)>5:
            print word
            #count= count+1


def getFileids():

    index=0
    for id in inaugural.fileids():
        index+=1
        if index==2:
            print id # print the president name
            print len(inaugural.words(id)) #print the # of words
        if index==14:
            print id # print the president name
            print len(inaugural.words(id)) #print the # of words


def getGraphs():
    index =0
    for id in inaugural.fileids(): #prob(-14)
        index+=1
        ww= inaugural.raw(id).lower()
        num_war=ww.count('war')
        num_america=ww.count('america')
        num_economy=ww.count('economy')
        num_world=ww.count('world')
        plot(index, num_war,'mo') #war
        plot(index, num_america,'go') #america (increasing)
        plot(index, num_economy,'ro') #ecomony
        plot(index, num_world,'bo') #world (increasing)
        xlabel('index, purple-war, green-america, red-economy, world-blue')
        ylabel('the frequency of the words used')
    show()




def graphWords():
    index=0
    for id in inaugural.fileids():
        index+=1
        nchar=len(inaugural.raw(id))*1.0
        nword=len(inaugural.words(id))*1.0
        nsent=len(inaugural.sents(id))*1.0
        nvoc=len(set(w.lower() for w in inaugural.words(id)))*1.0
        a = nchar/nword
        b=nword/nsent
        c=nword/nvoc
        plot(index,a,'mo') #purple color
        plot(index,b,'go') #green color
        plot(index,c,'ro') #red color

        xlabel('index, from Washington to Obama (purple - character/word), (red - word/vocab)')
        ylabel('Average numbers (green - word/sentence)')
    show()

#graphWords()


#getGraphs()
#getFileids()
#getWords()
