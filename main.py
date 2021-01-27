from Resources.quotes_fetch import Quotes
from bots.config import create_api
from post import posting
from bots.tags import check_mentions
from bots.direct_message import direct_message_initial
import time

api = create_api()
quote_class = Quotes()
quote_author = quote_class.random_quote_fav()
quote = "\"" + quote_author[0] + "\" " + "- " + quote_author[1]


def tags(api):
    last_id = 1
    while True:
        last_id = check_mentions(api,last_id,quote)

def message(api):
    while True:
        direct_message_initial(api)

def post(api):
    while True:
        posting(api)

def retweet_fun(api):
    while True:
        retweet_fav(api)