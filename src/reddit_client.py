import praw
from configparser import ConfigParser
import logging


# Function to create a Reddit client using credentials from config.ini
def get_reddit_client():
    """Creates and returns a Reddit API client using credentials from config/config.ini"""

    # Load credentials from config.ini
    config = ConfigParser()
    config.read('config/config.ini')

    try:
        # Create and return the Reddit client
        reddit = praw.Reddit(
            client_id=config['REDDIT']['client_id'],
            client_secret=config['REDDIT']['client_secret'],
            user_agent=config['REDDIT']['user_agent']
        )
        logging.info("Successfully authenticated with Reddit API.")
        return reddit

    except Exception as e:
        logging.error(f"Error while creating Reddit client: {str(e)}")
        raise


# Function to get the top post from a specified subreddit
def get_top_post(subreddit_name):
    """Fetches the top post from the specified subreddit of the day and returns the title and URL."""

    try:
        # Initialize the Reddit client
        reddit = get_reddit_client()

        # Access the subreddit
        subreddit = reddit.subreddit(subreddit_name)

        # Fetch the top post of the day
        top_post = next(subreddit.top('day', limit=1))  # Get the top post for the day

        # Log the successful fetch
        logging.info(f"Fetched top post from r/{subreddit_name}: {top_post.title}")

        # Return the title and URL of the post
        return top_post.title, top_post.url

    except Exception as e:
        logging.error(f"Error fetching top post from r/{subreddit_name}: {str(e)}")
        raise
