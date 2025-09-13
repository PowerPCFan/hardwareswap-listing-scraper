import modules.splash as splash
from modules.config.configuration import config, local_version
from modules.colors.ansi_codes import RESET, BLUE, YELLOW, LIGHT_CYAN, ORANGE, ansi_is_supported


def print_welcome_text():
    welcome = "Welcome to the HardwareSwap Listing Scraper"
    username = f"u/{config.reddit_username}"
    dashes = "-" * (len(welcome) + len(username))

    mode = 'Firehose' if config.mode == 'firehose' else 'Match' if config.mode == 'match' else 'Match LLM'

    print(f"\n{dashes}")
    splash.print_splash_text_background(color=ansi_is_supported)
    print(f"\n{dashes}")
    print(f"{welcome}, {BLUE}{username}!{RESET}")
    print(f"Version: {ORANGE}{local_version}{RESET}")
    print(f"Mode: {LIGHT_CYAN}{mode}{RESET}")
    print(f"Press {YELLOW}Ctrl+C{RESET} to exit.")
    print(f"{dashes}")
