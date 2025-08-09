import praw
from praw.models import Subreddit, Submission, Redditor
from modules.config.configuration import config
from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported

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
