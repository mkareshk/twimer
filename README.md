# twimer
Stream Tweets into Your Favorite Databases

[![Build Status](https://circleci.com/gh/owhadi/twimer.svg)](https://app.circleci.com/pipelines/github/owhadi)

Analyzing tweets reveals very interesting insights about events in a specific time and location, people's opinions 
about the news, etc.
twimer aims to make the data collection easier for you so you can focus on your analysis only!

twimer helps you to store tweets with certain keywords and from specific geographic regions into JSON files or database 
systems in an easy way.

## Twitter API
To use this project, you need to obtain _CONSUMER_KEY_, _CONSUMER_SECRET_, _ACCESS_TOKEN_, _ACCESS_TOKEN_SECRET_ 
from [Twitter Developer](https://developer.twitter.com/en).

## Installation
Simply install this package by running the following command:
 ```bash
pip install twimer 
```

## Usage
In the current version, you can stream the tweets using keywords and store them in files (JSON and JSON.tar.gz)
and MongoDB database.

- To store the tweets as JSON (tar.gz) files into `my_path` directory:
```python
import twimer

stream_tweet = twimer.Twimer(CONSUMER_KEY, 
                             CONSUMER_SECRET, 
                             ACCESS_TOKEN, 
                             ACCESS_TOKEN_SECRET, 
                             storage_method='file/targz', 
                             file_path=my_path)
stream_tweet.start_streaming(filters=['keyword1', 'keyword2'])
```

- To store the tweets in a MongoDB database using url `my_url`:
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

The `my_url` is in _mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]_ format.

## Contribution
You are very welcome to contribute to this project with your code (as pull-requests), mention the bugs or ask for new 
features (as GitHub Issues), or just tell your friends about it! 

You can also directly contact me by [email](moein.owhadi@gmail.com).
 

