from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "707079396922773504-Vr0Com9qRPepTEudQhq03Lhe8zYAXwv"
access_token_secret = "ycmLrMJBehXUa05aha3ETjDyvhhHeKrVJ2DVpAK9CEkyU"
consumer_key = "DYbUqhruqZZbqiEU0smju3sRk"
consumer_secret = "JpxYvtCtHIsV3E0IuRWG9DvhejpsdqHq8SxL75fM5hDt88nFAx"


class StdOutListener(StreamListener):
    def on_data(self, data):
        outfile.write(data)
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    outfile = open('../Data/streaming_data.txt', 'w')
    stream = Stream(auth, StdOutListener())

    # set search key word
    stream.filter(track=['apple'])



