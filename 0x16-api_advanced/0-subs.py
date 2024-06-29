#!/usr/bin/python3
'''
Script returns number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
#    url = f"https://www.reddit.com/r/{subreddit}/about.json".format(subreddit)
#    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0.0 (by /u/Tshepiso)"}
    try:

        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except requests.RequestException:
        return 0
