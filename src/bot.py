from reddit_client import fetch_top_post_from_reddit
from twitter_client import post_tweet

def main():
    subreddit = 'interestingasfuck'
    top_post = fetch_top_post_from_reddit(subreddit)
    if top_post:
        tweet_text = top_post['title']

        if top_post.get('image_url'):
            tweet_text += f" {top_post['image_url']}"
            print("Image URL found:", top_post['image_url'])
        elif top_post.get('video_url'):
            tweet_text += f" {top_post['video_url']}"
            print("Video URL found:", top_post['video_url'])
        elif top_post.get('post_url'):
            tweet_text += f" {top_post['post_url']}"
            print("Post URL found:", top_post['post_url'])
        else:
            print("No valid media found.")

        # Post tweet
        post_tweet(tweet_text)
    else:
        print("No valid top post found.")

if __name__ == "__main__":
    main()
