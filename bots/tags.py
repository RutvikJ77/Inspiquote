"""
Provides Tag functionality to the bot.
"""
import logging
import tweepy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api,last_id,quote):
    """
    Retrieves tags from timeline retweets and favorites the tweet
    returns: updated id
    """
    try:
        logger.info("Retrieving mentions")
        new_last_id = last_id
        for tweet in tweepy.Cursor(api.mentions_timeline,last_id = last_id).items():
            new_last_id = max(tweet.id,new_last_id)
            if tweet.in_reply_to_status_id is not None:
                continue
            if not tweet.favorited and not tweet.retweeted:
                try:
                    logger.info("Answering to %s", tweet.user.name)
                    logger.info("Fav/Retweeting to %s", tweet.user.name)
                    tweet.favorite()
                    logger.info("Tweet retweeted")
                    tweet.retweet()
                    api.update_status(status="Thank You!😄 @" + tweet.user.screen_name
                    + " , here is another quote for you " + quote
                    ,in_reply_to_status_id=tweet.id)
                except Exception:
                    logger.error("Error on fav and retweet.",exc_info=True)
        return new_last_id
    except Exception:
        logger.warning("Fetching new tag post error")
        return None
