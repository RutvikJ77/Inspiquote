import tweepy
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api,last_id,quote):
    """
    
    """


    logger.info("Retrieving mentions")
    try:
        new_last_id = last_id
        for tweet in tweepy.Cursor(api.mentions_timeline,last_id = last_id).items():
            new_last_id = max(tweet.id,new_last_id)
            if tweet.in_reply_to_status_id is not None:
                continue
            logger.info(f"Answering to {tweet.user.name}")
            logger.info(f"Fav/Retweeting to {tweet.user.name}")
            if not tweet.favorited:
                try:
                    tweet.favorite()
                except Exception as e:
                    logger.error("Error on fav", exc_info = True)
            if not tweet.retweeted:
                try:
                    tweet.retweet()
                except Exception as e:
                    logger.error("Error on fav and retweet",exc_info=True)
            text = "Thank You!😄 @" + tweet.user.screen_name + " Here is another quote for you " + quote
            api.update_status(status=text,in_reply_to_status_id=tweet.id)
        return new_last_id
    except:
        logger.warning("Fetching new tag post error")
    


# Local file testing purpose
# def main():
#     api = create_api()
#     last_id = 1
#     while True:
#         last_id = check_mentions(api, last_id,"\"Where there is a will there is a way.\"")
#         logger.info("Waiting...")
#         time.sleep(60)

# if __name__ == "__main__":
#     main()