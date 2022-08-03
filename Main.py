import Credentials
import tweepy
import json
import pandas as pd
import re


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
    dataFrame['Tweets'] = dataFrame['Tweets'].apply(RemovePunctuation)
    print(dataFrame.head())


def RemovePunctuation(tweet):
    return re.sub(r'\W+', ' ', tweet)


main()
