import tweepy
from configparser import ConfigParser
import logging


# Function to authenticate and get the Twitter API client
def get_twitter_client():
    """Creates and returns a Twitter API client using credentials from config/config.ini."""

    # Load credentials from config.ini
    config = ConfigParser()
    config.read('config/config.ini')

    try:
        # Set up OAuth1 authentication using the credentials
        auth = tweepy.OAuth1UserHandler(
            consumer_key=config['TWITTER']['api_key'],
            consumer_secret=config['TWITTER']['api_secret_key'],
            access_token=config['TWITTER']['access_token'],
            access_token_secret=config['TWITTER']['access_token_secret']
        )

        # Create the API client
        twitter_api = tweepy.API(auth)

        # Test the authentication by getting your account details
        twitter_api.verify_credentials()
        logging.info("Successfully authenticated with Twitter API.")

        return twitter_api

    except Exception as e:
        logging.error(f"Error while creating Twitter client: {str(e)}")
        raise


# Function to post a tweet
def post_to_twitter(message):
    """Posts a given message to the Twitter account."""

    try:
        # Initialize the Twitter client
        twitter_api = get_twitter_client()

        # Post the tweet
        twitter_api.update_status(message)

        # Log the successful post
        logging.info(f"Successfully posted to Twitter: {message}")

    except Exception as e:
        logging.error(f"Error posting to Twitter: {str(e)}")
        raise
