import matplotlib.pyplot as plt

#author:lethiraj


def twitter_sensitive1(file1,file2):
    data1 = open(file1)
    data2 = open(file2)
    hillary_state = []
    hillary_mention = []
    hillary_good = []

    for line in data1:
        coloumn = line.split()

        if coloumn[0] == 'HILLARY':
            for line in data1:
                coloumn = line.split()

                hillary_state.append(coloumn[0])
                hillary_mention.append(int(coloumn[2]))

    for line2 in data2:
        coloumn2 = line2.split()
        hillary_good.append(int(coloumn2[2]))

    hillary_bad = [hillary_mention[i] - hillary_good[i] for i in range(0, len(hillary_state))]

    print(sum(hillary_mention))
    print(sum(hillary_good))
    print(max(hillary_mention))
    print(float(452/17799)*100)

    pos = range(0, len(hillary_state))
    x = range(len(hillary_state))

    width = 0.25

    plt.xticks(x, hillary_state)
    plt.bar(x,hillary_good, width, alpha=0.5, color='blue', label='Good_Sentiments')
    plt.bar(x, hillary_bad, width, alpha=0.5, color='red', label='Bad/Neutral_sentiments', bottom=hillary_good)
    plt.xticks(range(0, len(hillary_state)))
    plt.ylabel('No of mentions in Twitter Feed')
    plt.xlabel('States')
    plt.title('Sentiment Analysis')
    plt.legend(['Good_sentiments', 'Bad/Neutral_Sentiments'], loc='upper right')
    plt.grid()
    plt.savefig('Hillary_sensitivity_analysis.png')

    plt.show()


twitter_sensitive1('mentions_by_state.txt','hillary_sentiment.txt')