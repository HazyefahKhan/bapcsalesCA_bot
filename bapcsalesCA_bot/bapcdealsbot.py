import praw
import tweepy
import time



CONSUMER_KEY = '5L93jHZlmluDqWvH2HoE0roqx'
CONSUMER_SECRET = '9MtSCo1c9SyaQquUTFxHJXWs04ZXllQnQPUkAAg2KPs2lTqhWI'
ACCESS_KEY = '1542208942138351624-OLazbj5P2fRwaukcAwKUoOCliVJAJ7'
ACCESS_SECRET = '3N1NslC0Pe5by1QIv9JsJT3n9RwXpZgauvVMUL9R8USCn'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

reddit = praw.Reddit(client_id = 'soVQ-TqjNMSR0YCy5ocFlw',
                     client_secret = 'm_ZkNVHaSMBdQi_rtsD9HpBO3OLh_w',
                     username = 'bapcsalesCA_bot',
                     password = 'hazyefah7',
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
    



