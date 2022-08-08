import Credentials
import json
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import datetime
import Visual
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
    query = '-RT abortion'
    tweets = client.search_recent_tweets(
        query=query, max_results=10)

    dataFrame = pd.DataFrame(
        [tweet.text for tweet in tweets.data], columns=['Tweets'])

    dataFrame['Tweets'] = dataFrame['Tweets'].apply(removePunctuation)

    dataFrame['Subjectivity'] = dataFrame['Tweets'].apply(getSubjectivity)

    dataFrame['Polarity'] = dataFrame['Tweets'].apply(getPolarity)

    dataFrame['Analyze'] = dataFrame['Polarity'].apply(analyze)
    #dataFrame.to_csv("dataFrame.csv", sep='\t')

    allWords = ' '.join(tweet for tweet in dataFrame['Tweets'])

    plot = Visual.Visual().CreateVisual(obj, dataFrame)
    print(plot.show())
    # print(createWordCloud(allWords))
    #print(getPercentage(dataFrame, ""))


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


def getPercentage(dataFrame, typeOfRating):
    if (typeOfRating.lower() == 'positive'):
        tweets = dataFrame[dataFrame.Analyze == 'Positive']
        tweets = tweets['Tweets']
    elif (typeOfRating.lower() == 'negative'):
        tweets = dataFrame[dataFrame.Analyze == 'Negative']
        tweets = tweets['Tweets']
    else:
        raise ValueError(
            "Please set typeOfRating to either positive or negative.")

    return str(round(tweets.shape[0]/dataFrame.shape[0]*100, 1)) + '%'


main()
