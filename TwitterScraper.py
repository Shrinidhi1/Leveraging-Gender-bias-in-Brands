import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import numpy as np

tweets_list2 = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#Gillette').get_items()):
    if i > 10:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])


# import csv
# import subprocess
# import json

# # search query
# query="#Gillette"

# # scrape tweets using snscrape
# command = f'snscrape --jsonl --max-results 1000 twitter-search "{query}" >2018_tweets_windies.json'
# subprocess.call(command, shell=True)

# # save tweets in CSV file
# with open("2018_tweets_windies.csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Date","Username","Tweet"])
#     with open("2018_tweets_windies.json", "r", encoding="utf-8") as jsonfile:
#         for line in jsonfile:
#             tweet = json.loads(line)
#             writer.writerow([tweet["date"],tweet["username"],tweet["content"],])
