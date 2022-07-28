import Credentials
import tweepy
import json


def main():
    # Creating jsonfile and abstracting the keys
    obj = Credentials.Credentials()
    jsonFile = Credentials.Credentials().ReadCredentialInfo(
        obj, 'TwitterDeveloperInfo.json')
    apiKey = jsonFile['api key']
    apiKeySecret = jsonFile['api key secret']
    bearerToken = jsonFile['bearer token']
    accessToken = jsonFile['access token']
    accessTokenSecret = jsonFile['access token secret']

    # open session with api
    client = tweepy.Client(bearer_token=bearerToken)
    result = 'from: BillGates -is:retweet'
    tweets = client.search_recent_tweets(query=result, max_results=10)

    for tweet in tweets.data:
        print(tweet.text)


main()
