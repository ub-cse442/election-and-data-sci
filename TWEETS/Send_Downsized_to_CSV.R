#skeleton code from documentation and adding customizations

library(httr)
library(devtools,lib.loc="~/R/x86_64-pc-linux-gnu-library/3.3")
library(base64enc) #for encoding/decoding data
library(rjson)  #for converting to json
library(streamR)
library(ROAuth)
library(ggplot2)
library(grid)

  for(i in 1:19)
  {
    
  print(paste("~/Desktop/Tweets_Downsized/pro_hillary/pro_hillarya",letters[i], sep = "" ))
  trump_tweets.df <- parseTweets(temp, simplify = FALSE, verbose = TRUE)
  write.csv(trump_tweets.df, file = "~/Desktop/Hillary19.csv")
  #data <- trtrump_tweets.df <- parseTweets("~/Desktop/Tweets_Downsized/pro_donald/donaldaa", verbose = FALSE)ump_tweets.df[- grep("NaN", trump_tweets.df$place_lat),]
  }

trump_tweets.df <- parseTweets("~/Desktop/Capturing_US_Tweets/love-donald-trump.json", verbose = FALSE)


