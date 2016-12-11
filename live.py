# -*- coding: utf-8 -*-

#  skeleton from tweepyFlujoMonitor
import tweepy
from tweepy.api import API
import os

API_KEY = 'pPIhAdO0U52jhQefecMfBbFWu'
API_SECRET = 'GYUtUVBJGmY1ukuK2fsgrgWhFvRkJRuE4uEutHrKiXZbiGJaVd'
ACCESS_TOKEN = '772218532801220608-FvglncyFsjQ4GvDqEwV7V98gDzCTyrA'
ACCESS_TOKEN_SECRET = 'd53zGf6203WfMR9rgrzZd02wceGrrZSIOGi5T6IMlCONy'
key = tweepy.OAuthHandler(API_KEY, API_SECRET)
key.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class Stream2Screen(tweepy.StreamListener):

    aList = []
    def __init__(self, api=None):
        self.api = api or API()
        self.n = 0
        self.m = 10

    def on_status(self, status):
        Stream2Screen.aList.append(status.text.encode('utf8'))
        #print status.text.encode('utf8')
        self.n = self.n+1
        if self.n < self.m:
            return True
        else:
            myfile = open('/home/ben/Desktop/CSE442/keepCount.txt','r')
            reader =myfile.readline()
            count = int(reader)
            tweetOut = myfile.read()
            myfile.close()
            for aValue in Stream2Screen.aList:
	        if('is good' in aValue or 'love him' in aValue or 'good guy' in aValue or 'nice guy' in aValue or 'make america great again' in aValue or 'sweet' in aValue or 'awesome' in aValue or 'badass' in aValue):
		    tweetOut = aValue
                    count = count + 1
            myfile = open('/home/ben/Desktop/CSE442/keepCount.txt', 'w')
            counter = str(count)
	    myfile.write(counter)
            myfile.write('\n')
            myfile.write(tweetOut)
            myfile.close()
            if(1 == True):
             	print ''' <!DOCTYPE html><html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>Live Stream</title>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Open+Sans">
<style>

body {
    font-family: 'Open Sans', sans-serif;
    font-size: 14px;
}

.top {
  height: 25px;
}

.bottom {
  height: 100px;
}

.background {
  overflow: auto;
  background-color: #F8F8F8;
  background-size: 110vw;
  background-attachment: scroll;
  height: 100vh;
}

.gap {
  height: 20px;
}

.active a {
    background-color: #123C62 !important;
}

* {
  border-radius: 0 !important;
}

.dropdown-menu {
  box-shadow: none;

}

.dropdown-menu>li>a {
    color: white;
}


.dropdown-menu>li>a:hover, .dropdown-menu>li>a:focus {
    background-color: #123C62;
    color: white;
}

.navbar-nav > li > .dropdown-menu {
    background-color: #222222;
}

</style>
</head>
<body background ="https://naturalhistory.si.edu/arctic/isc18/images/EastFront_night.jpg"><div>

 <!-- <div class="gap"></div> -->
  <nav class="navbar navbar-inverse" role="navigation">
    <div class="container-fluid white-container text-center">
      <ul class="nav navbar-nav">
        <li><a href="index.html">Home</a></li>

        <li class="dropdown">
            <a class="dropdown-toggle" data-toggle="dropdown" href="#">Data<span class="caret"></span></a>
            <ul class="dropdown-menu">
            <li><a href="data_2000.html">2000 Data</a>
            <li><a href="data_2004.html">2004 Data</a>
            <li><a href="data_2008.html">2008 Data</a>
            <li><a href="data_2012.html">2012 Data</a>
            <li><a href="data_2016.html">2016 Data</a>

            </ul>
        </li>


        <li><a href="twitter_analysis.html">Twitter Analysis</a></li>
        <li><a href="speech_analysis.html">Speech</a></li>
	<li class="active"><a href="Live_Stream.html">Live Stream</a></li>

    </div>
  </nav>






  </div>



    <div class="container-fluid white-container text-center">
        <br><br>
        <font color="silver"><h2>Positive Tweets Mentioning Donald Trump Since December 1st, 2016:</h2></font>
	<font color="white"><h1>'''
                print count
	        print '''</h1></font>
	<font color = "silver"><h2>What Are Those Tweets Saying?</h2>
	<font color = "white"><h1>
	'''
	        print tweetOut
	        print '''</h1>

        <!--<img src="./speech_analysis_files/words_count.png" alt="words_count" style="width:600px;height:500px;">
        <br><br>-->



    
  </div>


  <div class="bottom"></div></div>

</body>
</html>  '''
        return False

stream = tweepy.streaming.Stream(key, Stream2Screen())
#stream.filter(track=['donald trump','Donald Trump', 'donald Trump', 'Donald trump', 'trump', '#trump2016','the don', 'donald j trump'], languages=['en'])
stream.filter(track=['donald trump' , 'djt', 'DJT','trump', 'Trump', 'Donald Trump','trump2016'], languages = ['en'])
#yo

