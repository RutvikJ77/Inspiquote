from Resources.quotes_fetch import Quotes
from Resources.Image_fetch import GetImage
from Resources.Image_edit import image_edit
# from bots.config import create_api
import logging
import random
import tweepy
import time
import os
#Import config files if running as a single test file.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Get the quote details
def processing():
    """
    Fetches quotes, image and edits them.
    returns quote,author,image_credit,twitter_flag
    """
    quote = Quotes()
    try:
        today_quote = quote.quotable()
        query = quote.word_query_image(today_quote[0])
        logger.info("Quote - " + today_quote[0])
    except:
        today_quote = quote.quotes_fav()
        query = quote.word_query_image(today_quote[0])
        logger.info("Quote from favquotes - " + today_quote[0])


    # Retrieve the image details
    bg = GetImage()
    bg_image_details = bg.get_unsplash_img(query)
    logger.info(bg_image_details)

    # Image Editing
    quote = "\"" + today_quote[0] + "\" "
    author = "- " + today_quote[1]
    image_edit(bg_image_details[2],quote,author,query)

    #Checks whether Author has tweeter Id
    if bg_image_details[1] is None:
        image_credit = bg_image_details[0]
        twitter_flag = False
    else:
        image_credit = bg_image_details[1]
        twitter_flag = True

    # Deleting images from bg images
    try:
        os.remove("/app/bg images/"+query+".jpg") 
    except:
        logger.warning("Not able to delete the image")

    return quote,author,image_credit,twitter_flag

# Update it for post
def posting(api):
    try:
        image_path = '/app/test.jpg'
        quote,author,image_credit,twitter_flag = processing()
        if twitter_flag == True:
            tweet = quote + author + "\n\n 📸: " + "@" + image_credit
        else:
            tweet = quote + author + "\n\n 📸: " + image_credit
        api.update_with_media(image_path, tweet)
        logger.info("Tweet posted")
    except:
        logger.error("Unable to tweet post")

#change the image path

# Local testing
# def main():
#     api = create_api()
#     while True:
#         posting(api)
#         time.sleep(60)

# if __name__ =="__main__":
#     main()
