import configparser
import requests

config = configparser.ConfigParser()
config.read('../config/config.ini')

access_token = config['TWITTER']['access_token']

def post_tweet(tweet_text):
    url = 'https://api.twitter.com/2/tweets'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'text': tweet_text
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print('Tweet posted successfully')
        print(response.json())
    else:
        print(f'Error posting tweet: {response.status_code}')
        print(response.json())
