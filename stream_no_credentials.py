#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#For tweet parsing
import json
#To play the file
import subprocess
#Variables that contains the user credentials to access Twitter API 
access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 
#Set your triggers here
triggers = ["beta"]
#This is a basic listener that just prints received tweets
class StdOutListener(StreamListener):
#Function to perform on receiving data
    def on_data(self, data):
        #Load Json from tweet into twitJ object for parsing
        twitJ = json.loads(data)
        #Get text of the tweet
        tweet = twitJ['text']
        #Trigger counter
        ti = 0
        #Iterate through triggers if all triggers in the list are in the
        #tweet play sound clip
        for t in triggers:
            if t in tweet:
                ti += 1
        #If all triggers in tweet try to print tweet if that doesn't work
        #freak out but still play that sick-nasty trigger sound
        if ti == len(triggers):
            try:
                print(tweet)
            except:
                print("It don't work no more.")
            #Set trigger sound file, and method for playing file here (start on windows will play with
            #default player)
            subprocess.call([<play method>,<trigger sound path>], shell=True)
        return True
    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #Tracking list
    track = []
    #When script called ex. python stream.py hello python
    #the script will track the system arguments so #hello and #python in the preceding case
    for tag in sys.argv:
        track.append(str(tag))
    track = track[1:]
    #Lets you know what you're tracking
    print(track)
    stream.filter(track = track)
