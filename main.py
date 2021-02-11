from Resources.quotes_fetch import Quotes
from bots.config import create_api
from post import posting
from bots.tags import check_mentions
from bots.direct_message import direct_message_initial
from bots.retweet_fav import retweet_fav_post
import time

api = create_api()
quote_class = Quotes()
quote_author = quote_class.quotes_fav()
quote = "\"" + quote_author[0] + "\" " + "- " + quote_author[1]


def tags():
    last_id = 1
    last_id = check_mentions(api,last_id,quote)

def message():
    direct_message_initial(api)

def tweet_quote():
    api.update_status(quote)

def post():
    posting(api)

def retweet_fun():
    retweet_fav_post(api)