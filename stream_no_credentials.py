#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
import subprocess
#Variables that contains the user credentials to access Twitter API 
access_token = "709599859267997696-h44IFfG7SXvVNA5gfuFRSfnWjZHVzE9"
access_token_secret = "zAlD6AYEo7pa05b120Wvx8uXGhkESx4hqbMSFLt8JuKtu"
consumer_key = "61xHwzxtpdbQr1Dum7Iqx4sku"
consumer_secret = "pSAzVfWfjnGexFFvdxODU1Qiy9KT1cMkhwpEbCsjQCQHnGTZB4"

triggers = ["beta"]
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        twitJ = json.loads(data)
        tweet = twitJ['text']
        ti = 0
        for t in triggers:
            if t in tweet:
                ti += 1
        if ti == len(triggers):
            try:
                print(tweet)
            except:
                print("trouble")
            subprocess.call(['start','sf.mp3'], shell=True)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    subprocess.call(['start','sf.mp3'], shell=True)
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    track = []
    for tag in sys.argv:
        track.append(str(tag))
    track = track[1:]
    print(track)
    stream.filter(track = track)