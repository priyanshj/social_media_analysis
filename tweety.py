import tweepy
import csv

consumer_key = 'mGtfJEPztJUZDScjmkYTd4RSG'
consumer_secret = '6kaItRLCifHeEOOTJuM4lQqBagRNvkpM1uEIgV2wu6yh9QegLQ'
access_token = '4698385280-gqXsRJ84lSY0wl9dwJ2zC1tTRwhgYdLCCK4mAb3'
access_secret = 'v67ISq7U3tjcI1VGMlvsRr2LIG7s4cFfmKenQJqWzD4G4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('travel.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#rajasthan#travel",count=100,\
                           lang="en",\
                           
                           untill="2017-05-10").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
