import tweepy
import logging
import random
#Import the required config and time module for single file test.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def retweet_fav(api):
    """
    Retweets tweets with #motivation or #inspiration
    @param api - api object created from config
    """
    try:
        for tweet in tweepy.Cursor(api.search,q=random.choice(["#motivation","#inspiration"])).items(1):
            if not tweet.favorited and not tweet.retweeted:
                try:
                    logger.info("Tweet fav")
                    tweet.favorite()
                    logger.info("Tweet retweeted")
                    tweet.retweet()
                except Exception as e:
                    logger.error("Error on fav and retweet", exc_info=True)
    except tweepy.TweepError as e:
        logger.error(e.reason)

# Local testing purposes
# def main():
#     api = create_api()
#     while True:
#         retweet_fav(api)
#         time.sleep(10)

# if __name__ =="__main__":
#     main()