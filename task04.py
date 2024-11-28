import tweepy

# Replace with your own credentials from Twitter Developer Portal
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Collect tweets mentioning a brand or keyword
tweets = tweepy.Cursor(api.search, q='#BrandName', lang='en', since='2024-01-01').items(1000)

# Store tweet data in a list
tweet_data = []
for tweet in tweets:
    tweet_data.append(tweet.text)

