#!/usr/bin/python3
"""
recursive function using Reddit API
listing all articles and titles
"""
import requests


def recurse(subreddit, hot_list=[]):
    """functions that prints hot list articles"""
    urls = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "recursive-reddit-fetcher/0.1"}
    params = {"limit": 100}

    # pagination token if present
    if after:
        params['after'] = after

    # Make the request witihout following redirects
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    except requests.RequestException:
        return None

    # Check for valid response
    if response.status_code != 200:
        return None

    data = reponse.json().get('data', {})
    children = data.get('children', [])

    # Append titles to hot_list
    if params :
        for post in children:
            hot_list.append(post['data']['title'])

    # Recursively fetch next page if available
    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list if hot_list else None
