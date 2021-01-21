import random
import requests
from rake_nltk import Rake

ACCESS_KEY_QUOTES = '6761a7c0be915cd2c9e8d6fd49cb360c'
CATEGORY = ['motivation', 'inspiration', 'inspire', 'motivational', 'productive']


class Quotes:
    def quotes_fav(self):
        '''
        Fetches quotes from FavQuotes API from the category list
        returns a list of quote and author
        '''
        response = requests.get('https://favqs.com/api/quotes/',
                                params={'filter':random.choice(CATEGORY)},
                                headers={'Authorization':'Token token='+ACCESS_KEY_QUOTES})
        quote_list_json = response.json()
        return [quote_list_json['quotes'][0]['body'], quote_list_json['quotes'][0]['author']]

    def random_quote_fav(self):
        '''
        Fetches quote of the Day
        returns a list of quote and author
        '''
        response = requests.get('https://favqs.com/api/qotd')
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
        rank = Rake(max_length=1)
        rank.extract_keywords_from_text(quote)
        return rank.get_ranked_phrases()[0]

#Testing the quotes fetch method

# quote = quotable()
# print(quote[0])
# print(word_query_image(quote[0]))