

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = '27386210-rMytNktGI8L76GW3wEWkgtCdqqJjHyvjJDP4rKMKu'
access_token_secret = 'TZIw1JLWkcMVhtOu7QcqnheVLURWFs4qycUbw4CayLUJb'
consumer_key = '8MGjXHbUie0Jlhd9k0aPCeJ4f'
consumer_secret = 'N9PO34HSCwAw0oFW5xFebulJW6jXrBlxPSzh2SVomH5vOwDEwI'  

class StdOutListner(StreamListener):
    
    def on_data(self, data):
        print data
        return True
    
    def on_error(self, status):
        print status

if __name__ == '__main__':

    l = StdOutListner()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['taphouse', 'taphousegrill', 'pubcrawl'])



