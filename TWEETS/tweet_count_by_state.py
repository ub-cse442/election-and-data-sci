import csv
from pprint import pprint

def state_counter(csv_file_path_and_name, republican_state_dictionary, democratic_state_dictionary):
    with open(filePath,encoding = 'utf-8') as f:
        reader=csv.reader(f)
        for row in reader:
            if('love Donald Trump' in row[1] or'Trump2016' in row[1] or 'Trump' in row[1] or'hate hillary' in row[1] or 'fuck hillary' in row[1] or 'trump' in row[1] or 'the don' in row[1] or 'trump2016' in row[1] or '#buildawall' in row[1]):
                get_state = ((row[34]).split())[-1]
                if(len(get_state) ==2):
                    if not get_state in republican_state_Dict:
                        republican_state_Dict[get_state] = 1
                    else:
                        saveNum = republican_state_Dict.get(get_state)
                        saveNum = saveNum + 1
                        republican_state_Dict[get_state] = saveNum
            elif('love Hillary Clinton' in row[1] or'Hillary2016' in row[1] or 'hillary' in row[1] or 'Hillary Clinton' in row[1] or'hate Trump' in row[1] or 'fuck trump' in row[1] or 'imwithher' in row[1] or '#imwithher' in row[1] or 'hillary2016' in row[1] or 'clinton2016' in row[1]):
                get_state = ((row[34]).split())[-1]
                if(len(get_state) ==2):
                    if not get_state in democratic_state_Dict:
                        democratic_state_Dict[get_state] = 1
                    else:
                        saveNum = democratic_state_Dict.get(get_state)
                        saveNum = saveNum + 1
                        democratic_state_Dict[get_state] = saveNum

stateCounter = ''
republican_state_Dict = {}
democratic_state_Dict = {}
filePath = 'CSV_hillary/all_hillary.csv'
state_counter(filePath,republican_state_Dict,democratic_state_Dict)
filePath = 'CSV_donald/all_trump.csv'
state_counter(filePath,republican_state_Dict,democratic_state_Dict)

print('PRO DONALD STATE COUNTS:')
pprint(republican_state_Dict)
print('PRO HILLARY STATE COUNTS:')
pprint(democratic_state_Dict)


