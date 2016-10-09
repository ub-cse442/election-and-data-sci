#for capturing US tweets. Some of this code is from package documentation


library(httr)
library(devtools,lib.loc="~/R/x86_64-pc-linux-gnu-library/3.3")
library(base64enc) #for encoding/decoding data
library(rjson)  #for converting to jso
library(streamR)
library(ROAuth)
library(ggplot2)
library(grid)

api_key <- 'nlczeDhBe4m1WkmTWhGeWL9oS'
api_secret <- 'AsDWSyzPCZuzx5DTW6XRJoYi8x8qR6kvI4rbWrcqAA7T6MuQGT'
access_token <- '772218532801220608-FcHWRywnYynnFVIjf0GRe0uBNNfsSsH'
access_secret <- 'Xsy02Xjg9wK6wDqNFJHbYdao0xvY9y2TnxeOz8aEGikxW'
requestURL <- "https://api.twitter.com/oauth/request_token"
accessURL <- "https://api.twitter.com/oauth/access_token"
authURL <- "https://api.twitter.com/oauth/authorize"
my_oauth <- OAuthFactory$new(consumerKey = api_key, consumerSecret = api_secret, 
                             requestURL = requestURL, accessURL = accessURL, authURL = authURL)
my_oauth$handshake(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl"))
0548187
filterStream(file = "~/Desktop/hillary-clinton-good.json", track="hillary", locations = c(-125, 25, -66, 50), timeout = 3, 
             oauth = my_oauth)
filterStream(file = "~/Desktop/love-hillary-clinton.json", track="love+hillary+clinton", locations = c(-125, 25, -66, 50), timeout = 3, 
             oauth = my_oauth)


hillary_tweets.df <- parseTweets("~/Desktop/hillary-clinton-good.json", verbose = FALSE)
trump_tweets.df <- parseTweets("~/Desktop/donald-trump.json", verbose = FALSE)