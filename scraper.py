#!/usr/bin/env python3

# stdlib imports
import re as regexp
import time
from datetime import datetime
import sys

# The rest of the imports are at the bottom 
# after depchecker.check_dependencies() runs 
# to make sure all dependencies are installed

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
        client_id=config.reddit_id,
        client_secret=config.reddit_secret,
        user_agent=f"script:hardwareswap-listing-scraper (by u/{config.reddit_username})"
    )

    subreddit = reddit.subreddit("hardwareswap")

    print(f"{GREEN}Connected successfully.{RESET}")

    print_welcome_text()

    if config.mode == "firehose":
        firehose_mode(subreddit)
    elif config.mode == "match":
        match_mode(subreddit)
    elif config.mode == "match_llm":
        match_llm_mode(subreddit)
    else:
        raise Exception(f"{config.mode} is not a valid mode. Please ensure that your config.json file is properly set up.")

def check_variables():
    allowed_modes = ["firehose", "match", "match_llm"]
    
    if not config.reddit_id or not config.reddit_secret or not config.reddit_username:
        raise ValueError("There are missing variables in your config.json.\nPlease ensure all values are filled in using the instructions found in the README.")
    if config.mode == "match" and not (config.author_has or not config.author_wants):
        raise ValueError("You have match mode enabled, but have not specified any values for the author_has or author_wants keys.\nPlease switch to firehose mode to view all posts, or insert values in your config.json.")
    if config.push_notifications and not config.topic_name:
        raise ValueError("You have push notifications enabled, but have not specified a topic name.\nPlease set a topic name in your config.json file - see the README for instructions.")
    if config.sms and (not config.gmail_address or not config.app_password or not config.sms_gateway or not config.phone_number):
        raise ValueError("You have SMS notifications enabled but have not specified all of the required values.\nPlease ensure your config.json has all the proper values filled in.")
    if sum(bool(x) for x in [config.tinyurl, config.sl_expect_ovh, config.sl_powerpcfan_xyz]) > 1:
        raise ValueError("You cannot have more than one URL shortener enabled at once.\nPlease choose one and disable the others in your config.json file.")
    if config.mode not in allowed_modes:
        raise ValueError(f"Invalid mode specified in config.json. Allowed values are: 'firehose', 'match', 'match_llm'.")

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

def print_new_post(subreddit, author, h, w, url, utc_date, flair, title):
    j, pk, ck = get_karma_string(author) # use the full `author` var because the function needs more than just the name
    trades = get_trades_number(flair)
    
    date_posted = reddit_timestamp_creator(utc_date)

    if config.tinyurl:
        tinyurl = TinyURL()
        url = tinyurl.shorten(url, timeout=8)
    elif config.sl_expect_ovh:
        expect = SLExpectOVH()
        url = expect.shorten(url, timeout=8)
    elif config.sl_powerpcfan_xyz:
        ppc = SLPowerPCFanXYZ()
        url = ppc.shorten(url, timeout=8)
    else:
        url = url
    
    print("\n") # newline for spacing 
    print(f"New post by {BLUE}u/{author.name}{RESET} ({YELLOW}{trades}{RESET} {'trades' if trades != 1 else 'trade'} | joined {CYAN}{j}{RESET} | post karma {ORANGE}{pk}{RESET} | comment karma {PURPLE}{ck}{RESET}):")
    print(f"[H]: {GREEN}{h}{RESET}")
    print(f"[W]: {RED}{w}{RESET}")
    print(f"URL: {SUPER_LIGHT_CYAN}{url}{RESET}")
    print(f"Posted {WHITE}{date_posted}{RESET}")
    
    if config.push_notifications:
        ntfy.send_notification(title, url)

    if config.sms:
        sms.send_sms(url)
        
    if config.webhook:
        webhook.send_webhook(
            webhook_url = config.webhook_url,
            content = config.webhook_ping,
            username = "HardwareSwap Listing Scraper Alerts",
            embed = webhook.create_embed(
                color = "Dodger Blue",
                url = url,
                author = author.name,
                trades = trades,
                have = str(h).replace("[H]", "").strip(),
                want = str(w).replace("[W]", "").strip(),
                joined = j,
                post_karma = pk,
                comment_karma = ck,
                date_posted = date_posted
            )
        )

    # Sleep for a half second to make sure the script doesn't break
    # commented out because it's not really necessary here
    # time.sleep(0.5)

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
    username = f"u/{config.reddit_username}!"
    dashes = "-" * (len(welcome) + len(username))
    print(f"\n{dashes}")
    # splash.print_splash_text(WHITE=WHITE, BLUE=BLUE, RESET=RESET, color=ansi_is_supported)
    splash.print_splash_text_background(color=ansi_is_supported) # this one uses ansi background colors so it looks better
    print(f"\n{dashes}")
    print(f"{welcome}{BLUE}{username}{RESET}")
    print(f"Version: {ORANGE}{local_version}{RESET}")
    print(f"Mode: {LIGHT_CYAN}{'Firehose' if config.mode == 'firehose' else 'Match' if config.mode == 'match' else 'Match LLM'}{RESET}")
    print(f"Press {YELLOW}Ctrl+C{RESET} to exit.")
    print(f"{dashes}")

def parse_have_want(title):
    h_match = regexp.search(r'\[H\](.*?)\[W\]', title, regexp.IGNORECASE)
    w_match = regexp.search(r'\[W\](.*)', title, regexp.IGNORECASE)

    h = h_match.group(1).strip() if h_match else ""
    w = w_match.group(1).strip() if w_match else ""
    return h, w

def firehose_mode(subreddit):
    for submission in subreddit.stream.submissions(skip_existing = not config.retrieve_older_posts):
        h, w = parse_have_want(submission.title)
        print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)

def match_mode(subreddit):
    post_stream = subreddit.stream.submissions(skip_existing = not config.retrieve_older_posts)
    
    author_has_lower = [s.lower() for s in config.author_has]
    author_wants_lower = [s.lower() for s in config.author_wants]
    
    for submission in post_stream:
        h, w = parse_have_want(submission.title)
        if any(s in h.lower() for s in author_has_lower) and any(s in w.lower() for s in author_wants_lower):
            print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)

def match_llm_mode(subreddit):
    try:
        openrouter = ai.OpenRouter(api_key=config.openrouter_api_key)
        
        for submission in subreddit.stream.submissions(skip_existing = not config.retrieve_older_posts):
            h, w = parse_have_want(submission.title)
            title_replaced: str = str(submission.title).replace("[H]", "[Have]").replace("[W]", "[Want]").strip()
            
            response = openrouter.llm(author_has_llm_query=config.author_has_llm_query, author_wants_llm_query=config.author_wants_llm_query, title=title_replaced)

            if openrouter.is_match(response):
                print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)
            
            # sleep for 3 seconds to avoid API rate limiting, which would crash the script
            time.sleep(3)
            
    except Exception as e:
        raise Exception(f"{e.__dict__['body']['message']}")
        
if __name__ == "__main__":
    RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE = ("",) * 11
    try:
        import modules.dependency_checker as depchecker
        depchecker.check_dependencies()
        
        import modules.versioning_tools as versioning_tools

        remote_version = versioning_tools.get_remote_version()
        local_version = versioning_tools.get_local_version()
        
        # Local imports
        import modules.updater as updater
        import modules.splash as splash
        import modules.ai as ai
        import modules.config.config_tools as conftools
        from modules.notifications import ntfy, sms
        from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported
        import modules.discord.webhook as webhook
        from modules.url_shorteners import TinyURL, SLExpectOVH, SLPowerPCFanXYZ

        # Third-party imports
        import praw

        conftools.convert_py_to_json()
        conftools.ensure_all_values_are_present()

        from modules.config.configuration import config

        main()
    except KeyboardInterrupt:
        print(f"{YELLOW}\nExiting...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{'-' * 36}\n{RED}ERROR: An unexpected error occurred:{RESET}\n{'-' * 36}\n{e}")
        sys.exit(1)
