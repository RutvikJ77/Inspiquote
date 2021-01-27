import tweepy
import logging
import time

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()
# reply_options = [{"label":"Start ✅"},{"label":"No, Thank you! 👍"}]


#Todo:Implement quick options with new package

def direct_message_initial(api):
    try:
        logger.info("Retriveing followers")
        for follower in tweepy.Cursor(api.followers).items():
            if not follower.following:
                #logger.info(f"Following {follower.name}")
                follower.follow()
                logger.info(f"Sending message to {follower.name}")
                initial_message = "Hello " + follower.name + ''', Thank you 👍 for supporting InspiQuote. I will make sure you stay motivated 😁'''
                api.send_direct_message(follower.id_str,initial_message)
    except:
        logger.warning("direct_message-> Not able to send the message.")


#Todo: Implement selected approach for start and stop

# For performing local tests
# def main():
#     api = create_api() 
#     while True:
#         direct_message_initial(api)
#         logger.info("Waiting...")
#         time.sleep(10)

# if __name__ == "__main__":
#     main()