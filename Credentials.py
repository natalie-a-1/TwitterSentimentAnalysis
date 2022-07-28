import json
import tweepy
import textblob as TextBlob
import wordcloud as WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


class Credentials:

    @staticmethod
    def ReadCredentialInfo(self, file):
        file = open(file)
        jsonFile = json.load(file)
        return jsonFile
