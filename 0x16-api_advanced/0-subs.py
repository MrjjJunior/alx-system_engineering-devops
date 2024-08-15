#!/usr/bin/python3
'''
Script queries Reddit API and
return number of subcribers
'''
import requests


def number_of_subscribers(subreddit):
    ''' counts number of subs '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    #headers = {"User-Agent": "Mozilla/5.0"}
    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
