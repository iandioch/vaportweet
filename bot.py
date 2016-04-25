import tweepy
import random
import time

api = None # tweepy api
twitter_auth_file = 'twitter_auth.txt'
wordlist_file = 'wordlist.txt'
words = []
finished_words = set()
finished_word_file = 'finished_words.txt'

def append_file(filename, s):
    with open(filename, 'a') as f:
        f.write(s)
        f.write('\n')

def widetext(s):
    widechars = u"\ufeff\uff41\uff42\uff43\uff44\uff45\uff46\uff47\uff48\uff49\uff4a\uff4b\uff4c\uff4d\uff4e\uff4f\uff50\uff51\uff52\uff53\uff54\uff55\uff56\uff57\uff58\uff59\uff5a"
    d = ord('a')
    s = s.lower()
    return ' '.join([widechars[ord(c)-d+1] for c in s])

def tweet(s):
    t = widetext('vapor' + s)
    print t
    api.update_status(t)
    finished_words.add(s)
    append_file(finished_word_file, s)

if __name__ == '__main__':
    try:
        # load the twitter auth
        with open(twitter_auth_file, 'r') as f:
            auth_data = [l.strip() for l in f]

        with open(finished_word_file, 'r') as f:
            finished_words = set([l.strip() for l in f])

        with open(wordlist_file, 'r') as f:
            words = [l.strip() for l in f]

        auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
        auth.set_access_token(auth_data[2], auth_data[3])
        api = tweepy.API(auth)
    
        while True:
            word = 'help me'
            while True:
                word = random.choice(words)
                if word not in finished_words:
                    break
            tweet(word)
            time.sleep(10*60)

    except Exception as e:
        print 'Error during setup:'
        print e

