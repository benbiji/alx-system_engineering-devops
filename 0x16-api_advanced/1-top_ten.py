#!/usr/bin/python3
"""Print the titles of the 10 hottest posts on a given subreddit."""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced"}
    params = {"limit": 10}
    response = requests.get(
        url=url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    [print(t.get("data").get("title")) for t in results.get("children")]
