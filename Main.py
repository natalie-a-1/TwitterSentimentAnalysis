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
    result = 'abortion'
    tweets = client.search_recent_tweets(query=result, max_results=100)
    tweetList = []

    for tweet in tweets.data:
        tweetList.append(tweet.text)

    cleanList = RemovePunctuation(tweetList)
    dataFrame = pd.DataFrame(cleanList, columns=['Tweets'])
    print(dataFrame.head())


def RemovePunctuation(tweetList):
    newTweets = []
    for tweet in tweetList:
        cleanTweet = re.sub(r'\W+', ' ', tweet)
        newTweets.append(cleanTweet)
    return newTweets


main()
