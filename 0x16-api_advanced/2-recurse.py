#!/usr/bin/python3
"""
recursive function using Reddit API
listing all articles and titles
"""
import requests


def recurse(subreddit, hot_list=[]):
    """functions that prints hot list articles"""
    urls = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = 
