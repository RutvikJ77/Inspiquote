#from credentials import *
import logging
import tweepy
from os import environ
logger = logging.getLogger()

CONSUMER_KEY = environ["CONSUMER_KEY"]
CONSUMER_SECRET = environ["CONSUMER_SECRET"]
ACCESS_TOKEN = environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = environ["ACCESS_TOKEN_SECRET"]

def create_api():
    """
    Creates twitter api object for authentication
    returns api object
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth,wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api