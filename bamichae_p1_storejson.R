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


tweetsForTrump <- searchTwitter('Donald+Trump', n= 1000)
tweetsForHillary <- searchTwitter('Hillary+Clinton', n=1000)

dfTrump <- twListToDF(tweetsForTrump)
dfHillary <- twListToDF(tweetsForHillary)

jTrump <- toJSON(dfTrump, method = "C")
jHillary <- toJSON(dfHillary, method = "C")

write(jTrump, file = "~/Desktop/JsonTrump.txt")
write(jHillary, file = "~/Desktop/JsonHillary.txt")
