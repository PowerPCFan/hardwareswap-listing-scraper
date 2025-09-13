import praw
from praw.models import Subreddit, Submission, Redditor  # noqa: F401
from modules.config.configuration import config
from modules.colors.ansi_codes import RESET, GREEN, BLUE


def initialize() -> Subreddit:
    print(f"{BLUE}Connecting to Reddit...{RESET}")

    reddit = praw.Reddit(
        client_id=config.reddit_id,
        client_secret=config.reddit_secret,
        user_agent=f"script:hardwareswap-listing-scraper (by u/{config.reddit_username})"
    )

    subreddit = reddit.subreddit("hardwareswap")

    print(f"{GREEN}Connected successfully.{RESET}")

    return subreddit
