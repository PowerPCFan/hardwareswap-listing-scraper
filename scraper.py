import praw
import re as regexp
import time
from datetime import datetime
import sys
import requests
import modules.updater as updater
import modules.config_tools as conftools
from modules.tinyurl import TinyURL
from modules.gmail import Gmail
from modules.ansi import ansi_supported, ansi_codes

RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE = ansi_codes() if ansi_supported() else ("",) * 11

def main():
    updater.check_for_updates()
    
    print(f"{BLUE}Initializing variables...{RESET}")
    try:
        check_variables()
        print('') # print a singular new line if check_variables() passes in order to maintain spacing between the print statements
    except ValueError as e:
        print(f"{RED}{e}{RESET}\n")
        sys.exit(1)
    
    print(f"{BLUE}Connecting to Reddit...{RESET}")

    reddit = praw.Reddit(
        client_id=c.reddit_id,
        client_secret=c.reddit_secret,
        user_agent=f"script:hardwareswap-listing-scraper (by u/{c.reddit_username})"
    )
    
    subreddit = reddit.subreddit("hardwareswap")

    print(f"{GREEN}Connected successfully.{RESET}")

    print_welcome_text()
    
    if c.firehose:
        firehose_mode(subreddit)
    elif c.match:
        match_mode(subreddit)
    else:
        print(f"{RED}\nError: An unknown error occurred. Please ensure that your config.json file is properly set up. {RESET}")
        return

def check_variables():
    if not c.reddit_id or not c.reddit_secret or not c.reddit_username:
        raise ValueError("There are missing variables in your config.json.\nPlease ensure all values are filled in using the instructions found in the README.")
    if c.firehose == c.match:
        raise ValueError("You cannot have both firehose and match mode enabled or disabled at the same time.")
    if c.match and not (c.author_has or not c.author_wants):
        raise ValueError("You have match mode enabled, but have not specified any values for the author_has or author_wants keys.\nPlease switch to firehose mode to view all posts, or insert values in your config.json.")
    if c.push_notifications and not c.topic_name:
        raise ValueError("You have push notifications enabled, but have not specified a topic name.\nPlease set a topic name in your config.json file - see the README for instructions.")
    if c.sms and (not c.gmail_address or not c.app_password or not c.sms_gateway or not c.phone_number):
        raise ValueError("You have SMS notifications enabled but have not specified all of the required values. Please ensure your config.json has all the proper values filled in.")


def get_trades_number(flair: str) -> str:
    if isinstance(flair, str) and flair and flair.startswith("Trades: "):
        trades = flair.removeprefix("Trades: ").strip().lower()
    elif isinstance(flair, str):
        trades = flair.strip().lower()
    else:
        trades = "none"
        
    return "0" if trades == "none" else trades

def get_karma_string(author):
    j = reddit_account_age_timestamp_generator(author.created_utc)
    pk = author.link_karma
    ck = author.comment_karma
    
    return j, pk, ck

def send_notification(text, shorturl):
    headers={
        "X-Click": shorturl, # notification click action
        "X-Title": f"New listing on r/hardwareswap",
        "X-Priority": "3", # 1 = min, 2 = low, 3 = default, 4 = high, 5 = max
        "X-Markdown": "yes"
    }
    
    data = f"{text}\n\nListing URL: [{shorturl}]({shorturl})"
    data = data.encode(encoding='utf-8')
    
    try:
        requests.post(
            "https://ntfy.sh/" + c.topic_name,
            data=data,
            headers=headers
        )
    # just some generic error handling for common requests errors:
    except requests.exceptions.ConnectionError as e:
        print(f"{RED}A network error while sending notification: {e}{RESET}")
    except requests.exceptions.Timeout:
        print(f"{RED}Request timed out while trying to send notification.{RESET}")
    except requests.exceptions.HTTPError as e:
        print(f"{RED}An HTTP error occurred while sending notification: {e}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}An unexpected error occurred while sending notification: {e}{RESET}")
    except Exception as e:
        print(f"{RED}An unexpected error occurred while sending notification: {e}{RESET}")
        
def send_sms(shorturl):
    gmail = Gmail(c.gmail_address, c.app_password)

    recipient = f"{c.phone_number}@{c.sms_gateway}"
    subject = "" # no subject
    body = f"New listing on r/hardwareswap: {shorturl}"

    gmail.send_email(recipient, subject, body)

def print_new_post(subreddit, author, h, w, url, utc_date, flair, title):
    j, pk, ck = get_karma_string(author)
    trades = get_trades_number(flair)
    
    if c.tinyurl:
        tinyurl = TinyURL()
        url = tinyurl.shorten(url, timeout=8)
    else:
        url = url
    
    print(f"New post by {BLUE}u/{author.name}{RESET} ({YELLOW}{trades}{RESET} trades | joined {CYAN}{j}{RESET} | post karma {ORANGE}{pk}{RESET} | comment karma {PURPLE}{ck}{RESET}):")
    print(f"[H]: {GREEN}{h}{RESET}\n[W]: {RED}{w}{RESET}\nURL: {SUPER_LIGHT_CYAN}{url}{RESET}")
    print(f"Posted {WHITE}{reddit_timestamp_creator(utc_date)}{RESET}\n")
    
    if c.push_notifications:
        send_notification(title, url)
        
    if c.sms:
        send_sms(url)
        
    # Sleep for a half second to make sure the script doesn't break lol
    time.sleep(0.5)

# def reddit_timestamp_creator(unix_epoch):
#     now = int(time.time())
#     diff = now - int(unix_epoch)
#     if diff < 60:
#         return "just now"
#     elif diff < 3600:
#         minutes = diff // 60
#         return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
#     elif diff < 86400:
#         hours = diff // 3600
#         return f"{hours} hour{'s' if hours != 1 else ''} ago"
#     elif diff < 2592000:
#         days = diff // 86400
#         return f"{days} day{'s' if days != 1 else ''} ago"
#     elif diff < 31536000:
#         months = diff // 2592000
#         return f"{months} month{'s' if months != 1 else ''} ago"
#     else:
#         years = diff // 31536000
#         return f"{years} year{'s' if years != 1 else ''} ago"

def reddit_timestamp_creator(unix_epoch):
    # Convert to local datetime object
    dt = datetime.fromtimestamp(unix_epoch)
    
    # Extract components
    month = dt.month
    day = dt.day
    year = dt.year
    hour = dt.hour
    minute = dt.minute

    am_pm = "am" if hour < 12 else "pm"
    hour_12 = hour % 12 or 12

    return f"{month}/{day}/{year} at {hour_12}:{minute:02d} {am_pm}"

def reddit_account_age_timestamp_generator(unix_epoch):
    return time.strftime("%B %d, %Y", time.localtime(unix_epoch))

def print_welcome_text():
    welcome = f"Welcome to the HardwareSwap Listing Scraper, "
    username = f"u/{c.reddit_username}!"
    dashes = "-" * (len(welcome) + len(username))
    print(f"\n{dashes}")
    print(f"{welcome}{BLUE}{username}{RESET}")
    print(f"Mode: {WHITE}{'Firehose' if c.firehose else 'Match'}{RESET}")
    print(f"Press {YELLOW}Ctrl+C{RESET} to exit.")
    print(f"{dashes}\n")

def parse_have_want(title):
    h_match = regexp.search(r'\[H\](.*?)\[W\]', title, regexp.IGNORECASE)
    w_match = regexp.search(r'\[W\](.*)', title, regexp.IGNORECASE)

    h = h_match.group(1).strip() if h_match else ""
    w = w_match.group(1).strip() if w_match else ""
    return h, w

def firehose_mode(subreddit):    
    for submission in subreddit.stream.submissions(skip_existing = not c.retrieve_older_posts):
        h, w = parse_have_want(submission.title)
        print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)

def match_mode(subreddit):
    # for submission in subreddit.stream.submissions(skip_existing=True):
    for submission in subreddit.stream.submissions(skip_existing = not c.retrieve_older_posts):
        h, w = parse_have_want(submission.title)
        author_has_lower = [s.lower() for s in c.author_has]
        author_wants_lower = [s.lower() for s in c.author_wants]

        if any(s in h.lower() for s in author_has_lower) and any(s in w.lower() for s in author_wants_lower):
            print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)

if __name__ == "__main__":
    try:
        # check if config.py exists and if it does, convert to config.json
        conftools.convert_py_to_json()
        conftools.ensure_all_values_are_present()
        c = conftools.Config.load()
        
        main()
    except KeyboardInterrupt:
        print(f"{YELLOW}Exiting...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{'-' * 36}\n{RED}ERROR: An unexpected error occurred:{RESET}\n{'-' * 36}\n{e}")
        sys.exit(1)
