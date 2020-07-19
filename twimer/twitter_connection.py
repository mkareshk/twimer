import os
import json
import gzip
from pathlib import Path
from tweepy import OAuthHandler, Stream, StreamListener

from twimer.database import MongoDB

class TwitterConnection(StreamListener):

    def __init__(self, storage_method, storage_param, max_tweet_num):
        self.storage_method = storage_method
        self.storage_param = storage_param
        self.max_tweet_num = max_tweet_num
        self.tweet_num = 0

    def on_data(self, tweet):
        try:

            # retrieve a tweet
            tweet_id = json.loads(tweet)["id"]

            # storage
            if self.storage_method == 'file/plain':
                with open(Path(self.storage_param) / Path(f'{tweet_id}.json'), 'w') as fout:
                    fout.write(tweet)
            elif self.storage_method == 'file/targz':
                with gzip.GzipFile(Path(self.storage_param) / Path(f'{tweet_id}.json.gz'), 'w') as fout:
                    fout.write(tweet.encode('utf-8'))
            elif self.storage_method == 'mongodb':
                self.storage_param.insert_one(json.loads(tweet))
                print('mongodb success')

            # check the number of tweets so far
            self.tweet_num = self.tweet_num + 1
            if self.tweet_num > self.max_tweet_num:
                pass

        except Exception as e:
            print(f'runtime error: {e}')

    def on_error(self, status):
        print(status)
