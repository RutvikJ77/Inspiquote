
![InspiQuote](https://github.com/RutvikJ77/Inspiquote/blob/master/assets/cover-git.png)

[![GitHub issues](https://img.shields.io/github/issues/RutvikJ77/Inspiquote)](https://github.com/RutvikJ77/Inspiquote/issues)
[![GitHub license](https://img.shields.io/github/license/RutvikJ77/Inspiquote)](https://github.com/RutvikJ77/Inspiquote/blob/master/License.txt)
[![GitHub stars](https://img.shields.io/github/stars/RutvikJ77/Inspiquote)](https://github.com/RutvikJ77/Inspiquote/stargazers)

## About
**InspiQuote** is a Twitter bot which helps to motivate you on a daily basis. The bot was build with an aim to bring mental peace through the combination of amazing photographs linked with a keyword from the quote. 

### Go ahead and tag [@QuoteInspi](https://twitter.com/QuoteInspi) on Twitter for a motivational day.
[![Twitter](https://img.shields.io/twitter/url?color=none&label=Tweet%20%40QuoteInspi&logo=twitter&style=for-the-badge&url=https%3A%2F%2Ftwitter.com%2FQuoteInspi)](https://twitter.com/intent/tweet?text=Wow:&url=https://twitter.com/QuoteInspi)

## How it works and what it does?
➡️ It uses the REST API architecture and fetches quotes from the [Quotable](https://github.com/lukePeavey/quotable) and [favq's](https://favqs.com/api/). 

➡️ On fetching the quote it is parsed through [Rapid Automatic Keyword Extraction algorithm](https://github.com/csurfer/rake-nltk) (Rake-nltk) which gives a keyword from the quote. The extracted keyword is then passed to unsplash api for searching that relevant picture for the quote. 

➡️ After receiveing all the metrics and image, using Pillow library the image is edited with the quote and a watermark. As the editing process is complete it saves the image and is then posted on twitter using tweepy package. The bot is deployed via Heroku and scheduled to run at intervals using apscheduler.

➡️ Additionally it retweets messages from users with various motivation hashtags every 8 hours. Users who start following it receive a wonderful direct message for supporting it.

➡️ If tagged, it will send a reply with an additional quote.

## Architecture
```
├── License.txt
├── Procfile
├── README.md
├── Resources
│   ├── Image_edit.py
│   ├── Image_fetch.py
│   ├── __init__.py
│   └── quotes_fetch.py
├── assets
│   └── cover-git.png
├── bg\ images
│   └── random.txt
├── bots
│   ├── config.py
│   ├── direct_message.py
│   ├── retweet_fav.py
│   └── tags.py
├── clock.py
├── main.py
├── post.py
├── requirements.txt
├── server.py
```

### Requirements
- Apscheduler
- Tweepy
- Rake-nltk
- Urllib3
- Pillow
- Python==3.6
- Quotable API, Unsplash API, Favq's API

### Contributions
Always open for new features just create an issue. If want to add a new feature via pull request please make a separate branch for it.
> If you want to run it locally, add credentials.py with all the Twitter, Unsplash and FavQ's Keys 🔑. Import it to relevant files in Resources module with config.py in bots. Additional individual test file functions are provided as well.

## Wishing you a productive day 🎯 😁. If you got motivated considering giving it a 🌟.

