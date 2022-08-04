import Credentials
import json
import tweepy
# import textblob as TextBlob
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def main():
    # Creating jsonfile and abstracting the keys
    obj = Credentials.Credentials()
    jsonFile = Credentials.Credentials().ReadCredentialInfo(
        obj, 'TwitterDeveloperInfo.json')
    bearerToken = jsonFile['bearer token']

    # open session with api
    client = tweepy.Client(bearer_token=bearerToken)
    result = 'abortion'
    tweets = client.search_recent_tweets(query=result, max_results=5)

    dataFrame = pd.DataFrame(
        [tweet.text for tweet in tweets.data], columns=['Tweets'])

    dataFrame['Tweets'] = dataFrame['Tweets'].apply(removePunctuation)

    dataFrame['Subjectivity'] = dataFrame['Tweets'].apply(getSubjectivity)

    dataFrame['Polarity'] = dataFrame['Tweets'].apply(getPolarity)

    dataFrame['Analyze'] = dataFrame['Polarity'].apply(analyze)
    print(dataFrame)

    allWords = ' '.join(tweet for tweet in dataFrame['Tweets'])
    # createWordCloud(allWords)


def removePunctuation(tweet):
    tweet = re.sub(r'\W+', ' ', tweet)
    tweet = re.sub(r'#', ' ', tweet)
    tweet = re.sub(r'_', ' ', tweet)
    tweet = re.sub(r'https?:\/\/\S+', ' ', tweet)
    tweet = re.sub(r'RT[\s]+', ' ', tweet)
    return tweet.lower()


def getSubjectivity(tweet):
    return TextBlob(tweet).sentiment.subjectivity


def getPolarity(tweet):
    return TextBlob(tweet).sentiment.polarity


def analyze(score):
    if score > 0:
        return 'Positive'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Negative'


def createWordCloud(allWords):
    wordCloud = WordCloud(width=600, height=300, random_state=21,
                          max_font_size=100).generate(allWords)
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis('off')
    return plt.show()


main()
