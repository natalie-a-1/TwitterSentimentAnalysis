import Credentials
import json
import tweepy
# import textblob as TextBlob
from textblob import TextBlob
import wordcloud as WordCloud
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
    result = 'Bill Gates'
    tweets = client.search_recent_tweets(query=result, max_results=10)

    dataFrame = pd.DataFrame(
        [tweet.text for tweet in tweets.data], columns=['Tweets'])

    dataFrame['Tweets'] = dataFrame['Tweets'].apply(removePunctuation)

    dataFrame['Subjectivity'] = dataFrame['Tweets'].apply(getSubjectivity)

    dataFrame['Polarity'] = dataFrame['Tweets'].apply(getPolarity)

    print(dataFrame)


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


main()
