#import tweepy
from Resources.quotes_fetch import Quotes
from Resources.Image_fetch import GetImage



CONSUMER_KEY ="a0S4RKnB0kkH5ON4hrIuj6wKY"
CONSUMER_SECRET ="F1xxu9wjybFKqwndmnp3yd8nP3dftkMdpUCuw64i6KY6CB55yR"
ACCESS_TOKEN ="1325021734186049538-j7xD1Ja3vJUjGbwCggEJ6Yz2McmYu8"
ACCESS_TOKEN_SECRET ="LHSK4PFQV2C2F2iuhXxXTgVZjHxSyyvSTafwo6cMnnbkZ"


# image_path = 'test.jpg'

# Get the quote details
def quote_post():
    quote = Quotes()
    today_quote = quote.quotable()
    print("Quote - " + today_quote[0])
    print("Author - " + today_quote[1])


# Retrieve the image details







# Update it for post










# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api=tweepy.API(auth)
# tweet = '''The Sky is not the limit. Your mind is. - L.J Vanier\n.\n.\n 📸: Batu Gezer'''
# status = api.update_with_media(image_path, tweet)