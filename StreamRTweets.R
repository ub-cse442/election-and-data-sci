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
6908868
filterStream(file = "~/Desktop/hillary-clinton.json", track="hillary+clinton", locations = c(-125, 25, -66, 50), timeout = 10, 
             oauth = my_oauth)
filterStream(file = "~/Desktop/donald-trump.json", track="donald+trump", locations = c(-125, 25, -66, 50), timeout = 10, 
             oauth = my_oauth)

hillary_tweets.df <- parseTweets("~/Desktop/hillary-clinton.json", verbose = FALSE)
trump_tweets.df <- parseTweets("~/Desktop/donald-trump.json", verbose = FALSE)
map.data <- map_data("state")
hillary_points <- data.frame(x = as.numeric(hillary_tweets.df$lon), y = as.numeric(hillary_tweets.df$lat))
trump_points <- data.frame(x = as.numeric(trump_tweets.df$lon), y = as.numeric(trump_tweets.df$lat))
#points <- data.frame(x = as.numeric(tweets.df$lon), y = as.numeric(tweets.df$lat))
points <- points[points$y > 25, ]
trump_points<- d
ggplot(map.data) + geom_map(aes(map_id = region), map = map.data, fill = "white", 
  color = "grey20", size = 0.25) + expand_limits(x = map.data$long, y = map.data$lat) + theme(axis.line = element_blank(), axis.text = element_blank(), axis.ticks = element_blank(), 
        axis.title = element_blank(), panel.background = element_blank(), panel.border = element_blank(), 
        panel.grid.major = element_blank(), plot.background = element_blank(), 
        plot.margin = unit(0 * c(-1.5, -1.5, -1.5, -1.5), "lines")) + geom_point(data = points, aes(x = x, y = y), size = 1, alpha = 1/5, color = "darkblue")

