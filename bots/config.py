from credentials import *
import logging
import tweepy

logger = logging.getLogger()

def create_api():
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