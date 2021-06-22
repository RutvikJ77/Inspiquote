import logging
import os
from Resources.quotes_fetch import Quotes
from Resources.img_fetch import GetImage
from Resources.img_edit import image_edit
# from bots.config import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def processing():
    """
    Fetches quotes, image and edits them.
    returns quote,author,image_credit,twitter_flag
    """
    quote = Quotes()
    try:
        today_quote = quote.quotable()
        query = quote.word_query_image(today_quote[0])
        logger.info("Quote - %s", today_quote[0])
    except Exception:
        today_quote = quote.quotes_fav()
        query = quote.word_query_image(today_quote[0])
        logger.info("Quote from favquotes - %s", today_quote[0])


    # Retrieve the image details
    background = GetImage()
    bg_image_details = background.get_unsplash_img(query)
    logger.info(bg_image_details)

    # Image Editing
    quote = "\"" + today_quote[0] + "\" "
    author = "- " + today_quote[1]
    image_edit(bg_image_details[2],quote,author,query)

    # Checks whether Author has tweeter Id
    if bg_image_details[1] is None:
        image_credit = bg_image_details[0]
        twitter_flag = False
    else:
        image_credit = bg_image_details[1]
        twitter_flag = True

    # Deleting images from background images folder.
    try:
        os.remove("/app/bg images/" + query + ".jpg")
    except Exception:
        logger.warning("Not able to delete the image.")

    return quote,author,image_credit,twitter_flag

def posting(api):
    """
    Updates the Twitter account with a post.
    """
    try:
        image_path = '/app/test.jpg'
        quote,author,image_credit,twitter_flag = processing()
        if twitter_flag is True:
            tweet = quote + author + "\n\n 📸: " + "@" + image_credit
        else:
            tweet = quote + author + "\n\n 📸: " + image_credit
        api.update_with_media(image_path, tweet)
        logger.info("Tweet posted")
    except Exception:
        logger.error("Unable to tweet post")
