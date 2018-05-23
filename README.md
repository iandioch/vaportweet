# vaportweet

A twitter bot that embodies the aesthetic of our meagre existence

## Setup

Run `bot.py` to start the bot. 

It takes in its words from `wordlist.txt`.

A file is expected to exist called `twitter_auth.txt` with the following data:

```
consumer_key
consumer_secret
access_token
access_token_secret
```

It is also required that there be an empty file called `finished_words.txt` in the directory. This will store all the words the bot has already used.

