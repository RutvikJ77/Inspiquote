from Resources.quotes_fetch import Quotes
from bots.config import create_api
from post import posting
from bots.tags import check_mentions
from bots.direct_message import direct_message_initial
import time


quote_class = Quotes()
quote_author = quote_class.random_quote_fav()
quote = "\"" + quote_author[0] + "\" " + "- " + quote_author[1]

def main():
    api = create_api()
    last_id = 1
    while True:
        posting(api)
        time.sleep(60)

if __name__ =="__main__":
    main()