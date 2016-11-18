import matplotlib.pyplot as plt

#author:lethiraj


def twitter_sensitive(file1,file2):

    data1 = open(file1)
    data2 = open(file2)
    donald_state = []
    donald_mention = []
    donald_good = []




    for line in data1:
        coloumn = line.split()
        if coloumn[0] == 'DONALD':
            continue
        if coloumn[0] == 'HILLARY':
            break
        donald_state.append(coloumn[0])
        donald_mention.append(int(coloumn[2]))





    for line2 in data2:
        coloumn2 = line2.split()
        donald_good.append(int(coloumn2[2]))

    donald_bad = [ donald_mention[i] - donald_good[i] for i in range(0,len(donald_state))]

    print(sum(donald_mention))
    print((sum(donald_good)))
    print float(((172/53560)*100))

    pos = range(0, len(donald_state))
    x = range(len(donald_state))

    width = 0.25

    plt.xticks(x, donald_state)
    plt.bar(x, donald_good, width, alpha=0.5, color='blue', label='Good_Sentiments')
    plt.bar(x, donald_bad, width, alpha=0.5, color='red', label='Bad/Neutral_sentiments',bottom =donald_good)
    plt.xticks(range(0, len(donald_state)))
    plt.ylabel('No of mentions in Twitter Feed')
    plt.xlabel('States')
    plt.title('Sentiment Analysis')
    plt.legend(['Good_sentiments', 'Bad/Neutral_Sentiments'], loc='upper right')
    plt.grid()
    plt.savefig('Donald_sensitivity_analysis.png')
    plt.show()











twitter_sensitive('mentions_by_state.txt','sentiment_by_state.txt')