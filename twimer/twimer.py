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
        """
        Implements the main module to stream tweets and store them.
        :param consumer_key: Provided by Twitter API
        :param consumer_secret: Provided by Twitter API
        :param access_token: Provided by Twitter API
        :param access_token_secret: Provided by Twitter API
        :param storage_method: The storage destination that can be "file/plain", "file/targz", or "mongodb"
        :param file_path: The file path, if the storage_method is files
        :param mongo_url: The MongoDB connection if the storage_method is MongoDB. In this format:
            mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
        :param max_tweet_num: The maximum number of tweeter to get
        """

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

    def start_streaming(self, filters: str, languages: str = ['en']) -> None:
        """
        Start the process of streaming, given a list of filters and languages.
        :param filters: The list of filters, each of them is an string
        :param languages: The list of languages, each of them is an string
        """

        self.stream.filter(
            track=filters,
            languages=languages
        )
