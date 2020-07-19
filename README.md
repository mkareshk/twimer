# twimer
Stream Tweets into Your Favorite Databases

Analyzing tweets can reveal very interesting information about events in a specific time, people's opinions about the news, etc.
We, therefore, aim to make the data collection easier for you so you can focus on your analysis!

The goal of this project is to make collecting Twitter data easier. This is a wrapper for Tweepy Stream which help you 
store tweets with certain keywords and from specific geographic regions into JSON files for database systems.

## Twitter API
To use this project, you need to obtain _CONSUMER_KEY_, _CONSUMER_SECRET_, _ACCESS_TOKEN_, _ACCESS_TOKEN_SECRET_ 
from [Twitter Developer](https://developer.twitter.com/en)

## Installation
You can simply install this package by running the following command:
 ```bash
pip install twimer 
```

# Usage
In the current version, you can stream the tweets using their keywords and store them in files (JSON and JSON.tar.gz)
and MongoDB databases.

To store the tweets as JSON files in `my_path` directory:
```python
import twimer

stream_tweet = twimer.Twimer(CONSUMER_KEY, 
                             CONSUMER_SECRET, 
                             ACCESS_TOKEN, 
                             ACCESS_TOKEN_SECRET, 
                             storage_method='file/json', 
                             file_path=my_path)
stream_tweet.start_streaming(filters=['keyword1', 'keyword2'])
```

And to store the tweets in a MongoDB database using url `my_url`
```python
import twimer

stream_tweet = twimer.Twimer(CONSUMER_KEY, 
                             CONSUMER_SECRET, 
                             ACCESS_TOKEN, 
                             ACCESS_TOKEN_SECRET, 
                             storage_method='mongodb', 
                             mongo_url=mongo_url)
stream_tweet.start_streaming(filters=['keyword1', 'keyword2'])
```

