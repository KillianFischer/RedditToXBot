import configparser
import tweepy
import requests

# Load configuration
config = configparser.ConfigParser()
config.read('../config/config.ini')  # Ensure this path is correct

# Authenticate to Twitter
api_key = config['TWITTER']['api_key']
api_secret_key = config['TWITTER']['api_secret_key']
access_token = config['TWITTER']['access_token']
access_token_secret = config['TWITTER']['access_token_secret']

auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)

def upload_image(image_path):
    try:
        # Upload the image
        media = api.media_upload(image_path)
        print(f"Image uploaded successfully, media ID: {media.media_id}")
        return media.media_id
    except tweepy.TweepyException as e:
        print(f"Error uploading image: {e}")
        return None

def post_to_twitter_with_image(access_token, access_token_secret, media_id, tweet_text):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    payload = {
        'status': tweet_text,
        'media_ids': media_id
    }

    # Use requests to post to Twitter
    response = requests.post(url, params=payload, auth=(access_token, access_token_secret))

    return response
