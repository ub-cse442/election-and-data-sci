import csv

stateCounter = ''
stateDict = {}
with open('CSV_hillary/hillary_combined1.csv',encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if('hate hillary' in row[1] or 'fuck hillary' in row[1] or 'trump' in row[1] or 'the don' in row[1] or 'trump2016' in row[1]):
            get_state = ((row[34]).split())[-1]
            if(len(get_state) ==2):
                if not get_state in stateDict:
                    stateDict[get_state] = 1
                else:
                    saveNum = stateDict.get(get_state)
                    saveNum = saveNum + 1
                    stateDict[get_state] = saveNum
    sorted_states = sorted(stateDict)
