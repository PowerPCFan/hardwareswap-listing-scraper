import re as regexp
import modules.notifications.discord as discord
import modules.reddit as reddit
from modules.config.configuration import config
from modules.notifications import ntfy, sms
from modules.url_shorteners import TinyURL, SLExpectOVH, SLPowerPCFanXYZ
from modules.timestamp_generators import reddit_timestamp_creator, reddit_account_age_timestamp_generator
from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, SUPER_LIGHT_CYAN, ORANGE

def get_trades_number(flair: str) -> str:
    if isinstance(flair, str) and flair and flair.startswith("Trades: "):
        trades = flair.removeprefix("Trades: ").strip().lower()
    elif isinstance(flair, str):
        trades = flair.strip().lower()
    else:
        trades = "none"

    return "0" if trades == "none" else trades

def get_karma_string(author: reddit.Redditor) -> tuple[str, str, str]:
    j = reddit_account_age_timestamp_generator(author.created_utc)
    pk = author.link_karma
    ck = author.comment_karma

    return j, pk, ck

def parse_have_want(title: str) -> tuple[str, str]:
    h_match = regexp.search(r'\[H\](.*?)\[W\]', title, regexp.IGNORECASE)
    w_match = regexp.search(r'\[W\](.*)', title, regexp.IGNORECASE)

    h = h_match.group(1).strip() if h_match else ""
    w = w_match.group(1).strip() if w_match else ""
    return h, w

def print_new_post(subreddit: reddit.Subreddit, author: reddit.Redditor, h: str, w: str, url: str, utc_date: float, flair: str, title: str):
    j, pk, ck = get_karma_string(author) # use the full `author` var because the function needs the entire author object
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
        discord.send_webhook(
            webhook_url = config.webhook_url,
            content = config.webhook_ping,
            username = "HardwareSwap Listing Scraper Alerts",
            embed = discord.create_embed(
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
