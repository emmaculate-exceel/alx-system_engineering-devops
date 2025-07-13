#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    Args:
        subreddit (str): Name of the subreddit
    Returns:
        int: Number of subscribers, or 0 if invalid subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"user-agent": "Custom-Agent/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            data = response.json()
            result =data.get("data", {}).get("subscribers", 0)
            return result
        return 0
    except Exception:
        return 0

print(number_of_subscribers("python"))
