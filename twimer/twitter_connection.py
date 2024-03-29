import json
import time
import gzip
from pathlib import Path
from tweepy import Stream


class TwitterConnection(Stream):
    def __init__(
        self,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
        storage_method: str,
        storage_param: str,
        max_tweet_num: int,
        include_retweets: bool,
        include_replies: bool,
        reset_connection: int,
    ):
        """
        Implements connection to Twitter suing Tweepy Stream.
        :param storage_method: The storage destination that can be "file/plain", "file/targz", or "mongodb"
        :param storage_param: The parameter for storage, a directory path for files and connection URL for MongoDB
        :param max_tweet_num: The maximum number of tweets to get
        """

        super().__init__(
            consumer_key, consumer_secret, access_token, access_token_secret
        )

        self.storage_method = storage_method
        self.storage_param = storage_param
        self.max_tweet_num = max_tweet_num
        self.tweet_num = 0
        self.include_retweets = include_retweets
        self.include_replies = include_replies
        self.reset_connection = reset_connection

        self.time_init = time.time()

    def on_data(self, tweet: str) -> None:
        """
        Called when a tweet is retrieved and store it.
        :param tweet: The tweet as string
        """

        try:

            time_curr = time.time()
            time_diff = int((time_curr - self.time_init) / 60.0)
            if time_diff > self.reset_connection:
                self.time_init = time_curr
                exit()

            tweet = json.loads(tweet)

            # check if it's a retweet
            if not self.include_retweets and tweet["text"].startswith("RT @"):
                return

            # check if it's a reply
            if not self.include_replies and tweet["text"].startswith("@"):
                return

            # retrieve tweet ID
            tweet_id = tweet["id"]

            # storage
            if self.storage_method == "plain":
                with open(
                    Path(self.storage_param) / Path(f"{tweet_id}.json"), "w"
                ) as fout:
                    fout.write(tweet)
            elif self.storage_method == "targz":
                with gzip.GzipFile(
                    Path(self.storage_param) / Path(f"{tweet_id}.json.gz"), "w"
                ) as fout:
                    fout.write(tweet.encode("utf-8"))
            elif self.storage_method == "mongodb":
                self.storage_param.insert_one(tweet)

            # check the number of tweets so far
            self.tweet_num = self.tweet_num + 1
            if self.tweet_num > self.max_tweet_num:
                pass

        except Exception as e:
            print(f"runtime error: {e}")

    def on_error(self, status: str) -> None:
        """
        Called if there is an error, prints the status.
        :param status: The status as string
        """

        print(f"error: {status}")

    def on_limit(self, status: str) -> None:
        print(f"limit: {status}")

    def on_status(self, status):
        print(f"status: {status}")
