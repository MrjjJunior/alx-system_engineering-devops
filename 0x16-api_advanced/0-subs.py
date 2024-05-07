#!/usr/bin/python3
'''  '''
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    subreddit = input("Enter a subreddit: ")
    ptint(number_of_subscribers(subreddit))

