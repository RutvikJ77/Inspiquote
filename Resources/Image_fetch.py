import requests
import urllib.request as url
from PIL import Image

#Pixabay api - 19028782-fcb6ca5e87b47b77c6399d69a
UNSPLASH_ACCESS_KEY = 'VmQr4vB4YR8eeRKokj3HRWQjPK2tlRJ-qI3ZjblP-sc'


class GetImage:
    
    def get_unsplash_img(self,query_word = 'motivation')
        """
        Gets images from Unsplash and downloads it.
        @param query_word - ranked word
        returns list of metrics
        """
        orientation =random.choice(['landscape','portrait'])
        response = requests.get('https://api.unsplash.com/photos/random',
                            headers={'Authorization':'Client-ID '+UNSPLASH_ACCESS_KEY},params={'query':query_word,'orientation':'portrait'})
        img_data = response.json()
        img_url = img_data['links']['download']
        img_author = img_data['user']['name']
        img_twitter_username = img_data['user']['twitter_username']
        img_name = query+'.jpg'
        url.urlretrieve(img_url,img_name)
        return [img_name,img_author,img_twitter_username,orientation]


    def resize_img(self,image,orientation):
        """
        Resizes the image 
        """

        if orientation =='landscape':
            bg=Image.open(image)
            resize_bg = bg.resize((1200,675))
            resize_bg.save('bg images/resize_bg.jpg')
        else:
            bg=Image.open(image)
            resize_bg = bg.resize((640,960))
            resize_bg.save('bg images/resize_bg.jpg')

