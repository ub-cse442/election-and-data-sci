library(rjson)  #for processing json

importBernie <- fromJSON(paste(readLines('C:/Users/Ben/Desktop/Proj1 Q1/JsonBernie.json'), collapse="")) #import as json objects
importTrump <- fromJSON(paste(readLines('C:/Users/Ben/Desktop/Proj1 Q1/JsonTrump.json'), collapse=""))
imprtCruz <- fromJSON(paste(readLines('C:/Users/Ben/Desktop/Proj1 Q1/JsonCruz.json'), collapse=""))
importHillary <- fromJSON(paste(readLines('C:/Users/Ben/Desktop/Proj1 Q1/JsonHillary.json'), collapse=""))

