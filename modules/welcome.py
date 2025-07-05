import modules.splash as splash
from modules.config.configuration import config, local_version
from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported

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