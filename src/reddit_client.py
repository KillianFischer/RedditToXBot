import requests
import os

def fetch_top_post_from_reddit(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top/.json?limit=1&t=day"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    print(f"Requesting URL: {url}")
    print(f"Response status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        if data['data']['children']:
            top_post = data['data']['children'][0]['data']
            post_info = {
                'title': top_post['title'],
                'image_url': None,
                'video_url': None
            }

            if top_post['url'].endswith(('.jpg', '.png', '.gif', '.jpeg')):
                post_info['image_url'] = top_post['url']
            elif 'media' in top_post and 'reddit_video' in top_post['media']:
                post_info['video_url'] = top_post['media']['reddit_video']['fallback_url']
            elif 'preview' in top_post and 'reddit_video_preview' in top_post['preview']:
                post_info['video_url'] = top_post['preview']['reddit_video_preview']['fallback_url']
            else:
                post_info['post_url'] = f"https://www.reddit.com{top_post['permalink']}"

            return post_info
        else:
            print("No posts found in the subreddit.")
    else:
        print("Failed to fetch data from Reddit")

    return None
