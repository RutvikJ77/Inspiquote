"""
Provides Direct messaging functionality.
"""
import logging
import tweepy

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

def direct_message_initial(api):
    """
    Sends direct message to those follow.
    @param api - receives tweepy api object
    """
    try:
        logger.info("Retriveing followers")
        for follower in tweepy.Cursor(api.followers).items():
            if not follower.following:
                #logger.info(f"Following {follower.name}")
                follower.follow()
                logger.info("Sending message to %s",follower.name)
                initial_message = "Hello " + follower.name + '''
                , Thank you 👍 for supporting InspiQuote. 
                I will make sure you stay motivated 😁'''
                api.send_direct_message(follower.id_str,initial_message)
    except Exception:
        logger.warning("direct_message-> Not able to send the message.")

# TODO: Implement selected approach for start and stop
