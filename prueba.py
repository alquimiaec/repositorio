consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

authenticate = tweepy.OAutHandler(consumer_key, consumer_secret)

authenticate.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticate, wait_on_rate_limit = True)
