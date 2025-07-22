#!/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    fetching the top ten new on reddit
    """
    url = f"https://www.reddit.com/r/{subreddit}about.com"
    headers = {"user-agent":"Custom-Agent/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return "None"
        data = response.json()
        return data
    except Exception:
        return 0

print(top_ten("subreddit"))
