import random
import requests
from rake_nltk import Rake
from os import environ


# CATEGORY = ['motivation', 'inspiration', 'inspire', 'motivational', 'productive']
ACCESS_KEY_QUOTES = environ['ACCESS_KEY_QUOTES']

class Quotes:
    def quotes_fav(self):
        """
        Fetches quotes from FavQuotes API from the category list
        returns a list of quote and author
        """
        try:
            response = requests.get('https://favqs.com/api/quotes/',
                                    headers={'Authorization':'Token token='+ACCESS_KEY_QUOTES})
            quote_list_json = response.json()
            return [quote_list_json['quotes'][0]['body'], quote_list_json['quotes'][0]['author']]
        except:
            response = requests.get('https://favqs.com/api/quotes/',
                                    headers={'Authorization':'Token token='+ACCESS_KEY_QUOTES},verify=False)
            quote_list_json = response.json()
            return [quote_list_json['quotes'][0]['body'], quote_list_json['quotes'][0]['author']]



    def random_quote_fav(self):
        """
        Fetches quote of the Day
        returns a list of quote and author
        """
        response = requests.get('https://favqs.com/api/qotd',verify=False)
        quote_random = response.json()['quote']['body']
        quote_author = response.json()['quote']['author']
        return [quote_random, quote_author]

    def quotable(self):
        """
        Fetches quotes from quotable
        returns a list of quote and author
        """
        response = requests.get("https://api.quotable.io/random?maxLength=90")
        quote = response.json()['content']
        author = response.json()['author']
        return [quote, author]

    def word_query_image(self,quote):
        """
        Ranks the words from the quotes
        @param quote - type string
        returns a string
        """
        try:
            rank = Rake(max_length=1)
            rank.extract_keywords_from_text(quote)
            return rank.get_ranked_phrases()[0]
        except:
            return "random"

            
#Testing the quotes fetch method

# quote_class = Quotes()
# quote = quote_class.quotable()
# print(quote[0])
# print(quote_class.word_query_image(quote[0]))