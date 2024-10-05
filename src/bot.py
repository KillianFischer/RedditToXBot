from reddit_client import get_top_post
from twitter_client import post_to_twitter
import logging


def run_bot():
    try:
        # Fetch the top post from a specified subreddit
        subreddit_name = 'your_subreddit'
        title, url = get_top_post(subreddit_name)

        # Create the tweet content
        message = f"{title} {url}"

        # Post the tweet
        post_to_twitter(message)
        logging.info("Posted to Twitter successfully.")

    except Exception as e:
        logging.error(f"Error running bot: {str(e)}")


if __name__ == '__main__':
    run_bot()
