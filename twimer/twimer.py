from pathlib import Path
import json
import gzip
import os

from tweepy import OAuthHandler, Stream, StreamListener

from twimer.database import MongoDB
from twimer.twitter_connection import TwitterConnection


class Twimer:

    def __init__(self, consumer_key,
                 consumer_secret,
                 access_token,
                 access_token_secret,
                 storage_method=None,
                 file_path=None,
                 mongo_url=None,
                 max_tweet_num=100):


        # storage
        if storage_method in ('file/plain', 'file/targz'):

            if file_path is None:
                raise Exception('Pass file_path for the file/plain and file_json storage methods')
            elif not os.path.isdir(file_path):
                raise Exception(f'Directory {file_path} does not exist')

            self.storage_param = file_path

        elif storage_method == 'mongodb':
            if mongo_url is None:
                raise Exception('Pass mongo_url for the mongodb storage method')

            try:
                self.storage_param = MongoDB(mongo_url)
            except:
                print(f'MongoDB connection error. Could not connect to {mongo_url}')

        else:
            raise Exception(f'{storage_method} is not a valid storage method. '
                            f'The current options are: file/plain, file/targz, and mongodb')

        self.storage_method = storage_method
        self.max_tweet_num =max_tweet_num

        # tweepy Stream
        if True:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.tweeter_connection = TwitterConnection(self.storage_method, self.storage_param, self.max_tweet_num)
            self.stream = Stream(self.auth, self.tweeter_connection)
        else:
            print('Invalid API credentials')

    def start_streaming(self, filters, languages=['en']):
        self.stream.filter(
            track=filters,
            languages=languages
        )
