import requests
from twitter_client import post_to_twitter_with_image


def fetch_top_post_from_reddit(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top/.json?limit=1"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    print(f"Requesting URL: {url}")
    print(f"Response status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("Response data:", data)  # Debug print
        if data['data']['children']:
            top_post = data['data']['children'][0]['data']
            post_info = {
                'title': top_post['title'],
                'image_url': None,  # Default to None
                'video_url': None   # New field for video URL
            }

            # Check for image URLs
            if top_post['url'].endswith(('.jpg', '.png', '.gif')):
                post_info['image_url'] = top_post['url']
            # Check for video URLs
            elif 'media' in top_post and 'reddit_video' in top_post['media']:
                post_info['video_url'] = top_post['media']['reddit_video']['fallback_url']

            return post_info
    else:
        print("Failed to fetch data from Reddit")  # Debug print

    return None

def main():
    top_post = fetch_top_post_from_reddit('interestingasfuck')  # Modify as needed
    if top_post:
        if top_post['image_url']:
            # Proceed to post image to Twitter
            print("Image URL found:", top_post['image_url'])
            # Call your function to post to Twitter
            # post_to_twitter_with_image(..., top_post['image_url'], top_post['title'])
        elif top_post['video_url']:
            print("Video URL found:", top_post['video_url'])
            # You can choose to handle the video differently, e.g., just post a link or download and post
        else:
            print("No valid media found.")
    else:
        print("No valid top post found.")



if __name__ == "__main__":
    main()
