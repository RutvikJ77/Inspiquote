"""
Provides Retweet Functionality.
"""
import logging
import random
import tweepy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

hashtag = random.choice(["#motivation","#inspiration","#inspire"
                        ,"#wisdom","#growth","#success","#ambition"])

def retweet_fav_post(api):
    """
    Retweets tweets with #motivation or #inspiration
    @param api - api object created from config
    """
    try:
        for tweet in tweepy.Cursor(api.search,q=hashtag).items(1):
            if not tweet.favorited and not tweet.retweeted:
                try:
                    logger.info("Tweet fav")
                    tweet.favorite()
                    logger.info("Tweet retweeted")
                    tweet.retweet()
                except Exception:
                    logger.error("Error on fav and retweet", exc_info=True)
    except tweepy.TweepError as retweet_error:
        logger.error(retweet_error.reason)
