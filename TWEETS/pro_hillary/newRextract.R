library(httr)
library(devtools,lib.loc="~/R/x86_64-pc-linux-gnu-library/3.3")
library(twitteR)
library(base64enc) #for encoding/decoding data
library(rjson)  #for converting to json
library(ROAuth)

api_key <- 'nlczeDhBe4m1WkmTWhGeWL9oS'
api_secret <- 'AsDWSyzPCZuzx5DTW6XRJoYi8x8qR6kvI4rbWrcqAA7T6MuQGT'
access_token <- '772218532801220608-FcHWRywnYynnFVIjf0GRe0uBNNfsSsH'
access_secret <- 'Xsy02Xjg9wK6wDqNFJHbYdao0xvY9y2TnxeOz8aEGikxW'
setup_twitter_oauth(api_key,api_secret,access_token,access_secret)  #authorization with appropriate keys


tweetsForTrump <- searchTwitter("trump2016", n=5, geocode='39.8333333,-98.585522, 2680mi') 
#tweetsForHillary <- searchTwitter('hillary2016', n=100,geocode='39.8333333,-98.585522, 2680mi')


dfTrump <- twListToDF(tweetsForTrump)

while(nrow(newdata) < 10)
{

  tweetsForTrump <- searchTwitter("trump2016", n=10, geocode='39.8333333,-98.585522, 2680mi') 
  dfTrump <- twListToDF(tweetsForTrump)
  newdata <- dfTrump[!grep('trump2016', dfTrump$text),]
  newdata <- dfTrump[!grep('NaN', dfTrump$place_lat),]
}
jTrump <- toJSON(dfTrump, method = "C")
#jHillary <- toJSON(dfHillary, method = "C")

write.csv(dfTrump, file = "~/Desktop/JsonTrump.csv")
write.csv(dfHillary, file = "~/Desktop/JsonHillary.csv")


hillarycsv <-write.table(hillary_tweets.df, file = "~/Desktop/hillary.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
hillarycsv <-write.table(hillary_tweets.df, file = "~/Desktop/hillary.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")

