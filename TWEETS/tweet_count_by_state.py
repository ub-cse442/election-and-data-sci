import csv
from pprint import pprint

def state_counter(csv_file_path_and_name, republican_state_dictionary, democratic_state_dictionary):
    with open(filePath,encoding = 'utf-8') as f:
        reader=csv.reader(f)
        for row in reader:
            if('trump2016' in row[1] or'#buildawall' in row[1] or'#TrumpTrain' in row[1] or'trump' in row[1] or'Trump' in row[1] or'donald Trump' in row[1] or'Donald Trump' in row[1] or'donald trump' in row[1]):
                get_state = ((row[34]).split())[-1]
                if(len(get_state) ==2):
                    if not get_state in republican_state_Dict:
                        republican_state_Dict[get_state] = 1
                    else:
                        saveNum = republican_state_Dict.get(get_state)
                        saveNum = saveNum + 1
                        republican_state_Dict[get_state] = saveNum
            elif('hillary' in row[1] or'Hillary' in row[1] or'clinton' in row[1] or 'Clinton' in row[1] or'Hillary Clinton' in row[1]  or'hillary Clinton' in row[1] or 'Hillary clinton' in row[1] or 'imwithher' in row[1] or '#imwithher' in row[1] or 'hillary2016' in row[1] or 'clinton2016' in row[1]):
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
filePath = 'CSV_donald/all_trump1.csv'
state_counter(filePath,republican_state_Dict,democratic_state_Dict)
filePath = 'CSV_donald/all_trump2.csv'
state_counter(filePath,republican_state_Dict,democratic_state_Dict)

print('DONALD STATE COUNTS:')
pprint(republican_state_Dict)
print('HILLARY STATE COUNTS:')
pprint(democratic_state_Dict)


