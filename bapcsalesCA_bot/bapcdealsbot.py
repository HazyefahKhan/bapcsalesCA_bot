import praw
import tweepy
import time



CONSUMER_KEY = '<CONSUMER_KEY>'
CONSUMER_SECRET = '<CONSUMER_SECRET>'
ACCESS_KEY = '<ACCESS_KEY>'
ACCESS_SECRET = 'ACCESS_SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

reddit = praw.Reddit(client_id = '<CLIENT_ID',
                     client_secret = '<CLIENT_SECRET>',
                     username = '<ACC_USERNAME>',
                     password = '<ACC_PASSWORD>',
                     user_agent = 'Canadian PC Sales bot v1.0 by /u/bapcsalesCA_bot')

subreddit = reddit.subreddit("bapcsalescanada")

new_posts = subreddit.new()

def read_new_deals():

    new_deals = []
    with open("newdeals.txt") as new_deals_file:
        
        for line in new_deals_file:
            new_deals.append(line.strip())
    
    return new_deals

def post_tweet(deal_title, deal_url):
    tweet = f"{deal_title}\n{deal_url}"
    api.update_status(tweet)

def tweet():

    new_deals = read_new_deals()
    new_posts = subreddit.new(limit = 30)

    with open("newdeals.txt", "a") as new_deals_file:
        print(new_deals)

        for post in new_posts:
            if not post.stickied:
                if not(post.id) in new_deals:
                    post_tweet(post.title, post.url)

                    new_deals_file.write(f"\n{post.id}")

while True:
    tweet()
    time.sleep(300)
    



