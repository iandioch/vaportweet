import tweepy
import time

api = None # tweepy api
twitter_auth_file = 'twitter_auth.txt'

def tweet(s):
    api.update_status(s)

if __name__ == '__main__':
    try:
        # load the twitter auth
        with open(twitter_auth_file, 'r') as f:
            auth_data = [l.strip() for l in f]

        auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
        auth.set_access_token(auth_data[2], auth_data[3])
        api = tweepy.API(auth)
    
        while True:
            tweet('spam')
            time.sleep(10*60)

    except Exception as e:
        print 'Error during setup:'
        print e

