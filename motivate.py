from PIL import Image, ImageFont, ImageDraw
from rake_nltk import Rake
import os
import tweepy
import urllib.request as url
import wikiquotes
import requests
import wget
import random
ACCESS_KEY_UNSPLASH = 'VmQr4vB4YR8eeRKokj3HRWQjPK2tlRJ-qI3ZjblP-sc'
ACCESS_KEY_QUOTES = '6761a7c0be915cd2c9e8d6fd49cb360c'

consumer_key ="a0S4RKnB0kkH5ON4hrIuj6wKY"
consumer_secret ="F1xxu9wjybFKqwndmnp3yd8nP3dftkMdpUCuw64i6KY6CB55yR"
access_token ="1325021734186049538-j7xD1Ja3vJUjGbwCggEJ6Yz2McmYu8"
access_token_secret ="LHSK4PFQV2C2F2iuhXxXTgVZjHxSyyvSTafwo6cMnnbkZ"



CATEGORY = ['motivation','inspiration','inspire','motivational','productive']

#Quotes
def quotes():
    response = requests.get('https://favqs.com/api/quotes/',
                            params={'filter':random.choice(CATEGORY)},
                            headers={'Authorization':'Token token=6761a7c0be915cd2c9e8d6fd49cb360c'})
    quote_list_json = response.json()
    return quote_list_json['quotes'][0]['body'] + ' - ' + quote_list_json['quotes'][0]['author']


def random_quote():
    response = requests.get('https://favqs.com/api/qotd')
    quote_random = response.json()['quote']['body']
    quote_author = response.json()['quote']['author']
    return quote_random + " - " + quote_author

def wiki_quote():
    quote,author = wikiquotes.quote_of_the_day('english')
    return quote+' '+author


def word_query_image(quote):
    rank = Rake(max_length=1)
    rank.extract_keywords_from_text(quote)
    return rank.get_ranked_phrases()[0]

def unsplash_img(query):
    orientation =random.choice(['landscape','portrait'])
    response = requests.get('https://api.unsplash.com/photos/random',
                            headers={'Authorization':'Client-ID '+ACCESS_KEY_UNSPLASH},params={'query':query,'orientation':'portrait'})

    img_data = response.json()
    img_url = img_data['links']['download']
    img_author = img_data['user']['name']
    img_name = query+'.jpg'
    url.urlretrieve(img_url,img_name)
    return img_name,img_author,orientation

def resize_bg(image,orientation):
    if orientation=='landscape':
        bg=Image.open(image)
        resize_bg = bg.resize((#Add the coordinates))
        resize_bg.save('bg images/resize_bg.jpg')
    else:
        bg=Image.open(image)
        resize_bg = bg.resize((640,960))
        resize_bg.save('bg images/resize_bg.jpg')
      




def image_processing(image_path,quote):
    bg_img = Image.open(image_path)

    #Watermark
    draw_watermark = ImageDraw.Draw(bg_img)
    text = '@QuoteInspi'
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/HelveticaNeue.ttc",20)
    x = (wd//10)*4
    y = ht - (ht//10)
    draw_watermark.text((x,y),text,font=font,fill=(255,255,255,128))

    #Content
    quote = '"The sky is not the limit.\n\n         Your mind is."'
    draw_con = ImageDraw.Draw(bg_img)
    con_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Din Condensed Bold.ttf",55)
    text_con_wd,text_con_ht = draw_con.textsize(quote,con_font)
    draw_con.text((128,480),quote,font=con_font)

    #Author
    draw_author = ImageDraw.Draw(bg_img)
    aut_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/GillSans.ttc",30)
    aut_text = '-L.J Vanier'
    draw_author.text((wd//2.5,640),aut_text,font=aut_font)

def tweet_motivate(quote,image_path):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret)
    api=tweepy.API(auth)
    tweet = '''The Sky is not the limit. Your mind is. -L.J Vanier\n.\n.\n 📸: Batu Gezer'''
    status = api.update_with_media(image_path, tweet) 











# wiki_q = wiki_quote()
# print(wiki_q)
random_q = random_quote()
print(random_q)
query= word_query_image(random_q)
print(query)
img_name,img_author,orientation = unsplash_img(query)
resize_bg(img_name,orientation)
bg_path = 'bg images/test1.jpg'
image_processing(bg_path)
