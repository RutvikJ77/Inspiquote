import tweepy

consumer_key ="a0S4RKnB0kkH5ON4hrIuj6wKY"
consumer_secret ="F1xxu9wjybFKqwndmnp3yd8nP3dftkMdpUCuw64i6KY6CB55yR"
access_token ="1325021734186049538-j7xD1Ja3vJUjGbwCggEJ6Yz2McmYu8"
access_token_secret ="LHSK4PFQV2C2F2iuhXxXTgVZjHxSyyvSTafwo6cMnnbkZ"
image_path = 'test.jpg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)
tweet = '''The Sky is not the limit. Your mind is. - L.J Vanier\n.\n.\n 📸: Batu Gezer'''
status = api.update_with_media(image_path, tweet)