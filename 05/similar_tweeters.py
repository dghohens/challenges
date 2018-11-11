from collections import namedtuple
import sys
import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

NUM_TWEETS = 100

class UserTweets(object):

    def __init__(self, handle, max_id=None):
        """Get handle and optional max_id.
        Use tweepy.OAuthHandler, set_access_token and tweepy.API
        to create api interface.
        Use _get_tweets() helper to get a list of tweets.
        Save the tweets as data/<handle>.csv"""

        # This part is from the tweepy OAuth tutorial
        auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        try:
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            print('Error! Failed to get request token')
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

        self._tweets = list(self._get_tweets())
#        self._save_tweets()

    def _get_tweets(self):
        """Hint: use the user_timeline() method on the api you defined in init.
        See tweepy API reference: http://docs.tweepy.org/en/v3.5.0/api.html
        Use a list comprehension / generator to filter out fields
        id_str created_at text (optionally use namedtuple)"""
        tweet_tuple = namedtuple('Tweet', ['id_str','created_at','text'])
        json_tweets = self.api.user_timeline(handle, count = NUM_TWEETS)
        list_of_tweets = []
        for i in json_tweets:
            list_of_tweets.append(tweet_tuple(i['id_str'], i['created_at'], i['text']))
        return list_of_tweets

def break_into_words(all_tweets):
    ''' This function accepts all tweets from a UserTweets class as input.
    This outputs a list of strings from that class.'''
    all_words = []
    noise_words = [
        'much',
        'from',
        'dont',
        'nice',
        'guys',
        'them',
        'wait',
        'about',
        'awesome',
        'just',
        'posted',
        'this',
        'good',
        'post',
        'need',
        'with',
        'your',
        'into',
        'more',
        'also',
        'have',
        'like',
        'well',
        'think',
        'some',
        'cool',
        'pretty',
        'since',
        'last',
        'something',
        'cant',
        'love',
        'great',
        'doing',
        'then',
        'been',
        'want',
        'that',
        'what',
        'were',
        'where',
        'when',
        'which',
    ]

    for i in all_tweets:
        all_text = ''
        all_text2 = ''
        for j in i[2]:
            if j.isalpha() or j.isspace():
                    all_text += j.lower()

        for k in all_text:
            if k == '\n':
                all_text2 += ' '
            else:
                all_text2 += k

        for l in all_text2.split():
            if len(l) >= 4 and l not in noise_words:
                all_words.append(l)

    return all_words

def count_words(word_list):
    word_counts = {}
    freq_words = []

    for i in word_list:
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1

    for i in word_counts:
        if word_counts[i] > 1:
            freq_words.append(i)

    print(freq_words)
    pass

def similar_tweeters(user1, user2):
    pass

if __name__ == "__main__":
    handle = 'pybites'
    user = UserTweets(handle)
    count_words(break_into_words(user._get_tweets()))


'''    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
'''