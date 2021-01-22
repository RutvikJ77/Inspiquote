from Resources.quotes_fetch import Quotes
from Resources.Image_fetch import GetImage
import Resources.Image_edit as image_edit
import random
import tweepy


CONSUMER_KEY ="a0S4RKnB0kkH5ON4hrIuj6wKY"
CONSUMER_SECRET ="F1xxu9wjybFKqwndmnp3yd8nP3dftkMdpUCuw64i6KY6CB55yR"
ACCESS_TOKEN ="1325021734186049538-j7xD1Ja3vJUjGbwCggEJ6Yz2McmYu8"
ACCESS_TOKEN_SECRET ="LHSK4PFQV2C2F2iuhXxXTgVZjHxSyyvSTafwo6cMnnbkZ"


# image_path = 'test.jpg'

# Get the quote details

quote = Quotes()
today_quote = random.choice([quote.quotable(),quote.quotes_fav()])
query = quote.word_query_image(today_quote[0])
print("Quote - " + today_quote[0])
print(query)


# Retrieve the image details

bg = GetImage()
bg_image_details = bg.get_unsplash_img(query)
print(bg_image_details)



# Image Editing
quote = "\"" + today_quote[0] + "\""
author = "- " + today_quote[1]
image_edit(bg_image_details[2],quote,author)



# Update it for post











# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api=tweepy.API(auth)
# tweet = today_quote[0] + "\n.\n.\n 📸:"
# status = api.update_with_media(image_path, tweet)