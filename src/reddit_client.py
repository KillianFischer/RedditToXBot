import praw
import requests
import configparser
import os

# Initialize the config parser
config = configparser.ConfigParser()
config.read('../config/config.ini')

client_id = config['REDDIT']['client_id']
client_secret = config['REDDIT']['client_secret']
user_agent = config['REDDIT']['user_agent']

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

def get_top_post(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = list(subreddit.top(limit=1))

    if not top_posts:
        return None  # Handle the case where there are no posts

    top_post = top_posts[0]  # Get the first (and only) post from the list
    return {
        'title': top_post.title,
        'url': top_post.url,
        'score': top_post.score,
        'image_url': top_post.url  # Add the image URL (or any other relevant field)
    }

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image_filename = os.path.basename(image_url)  # Get the image filename from the URL
            image_path = os.path.join(save_path, image_filename)  # Construct the full file path
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Image downloaded and saved to: {image_path}")  # Confirm saving
            return image_path
        else:
            print(f"Error downloading image: {response.status_code}")  # Log the status code
            return None
    except Exception as e:
        print(f"Exception occurred while downloading the image: {e}")
        return None