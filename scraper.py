#!/usr/bin/env python3

import sys
# The rest of the imports are at the bottom 
# after depchecker.check_dependencies() runs 
# to make sure all dependencies are installed

def main():
    updater.check_for_updates()

    print(f"{BLUE}Initializing variables...{RESET}")
    try:
        variable_checker.check()
        print("") # print a singular new line if check() passes in order to maintain spacing between the print statements
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

    welcome.print_welcome_text()

    if config.mode == "firehose":
        modes.firehose(subreddit)
    elif config.mode == "match":
        modes.match(subreddit)
    elif config.mode == "match_llm":
        modes.match_llm(subreddit)
    else:
        raise Exception(f"{config.mode} is not a valid mode. Please ensure that your config.json file is properly set up.")
        
if __name__ == "__main__":
    RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE = ("",) * 11
    try:
        import modules.checks.dependency_checker as depchecker
        depchecker.check_dependencies()

        # Local imports
        import modules.welcome as welcome
        import modules.modes as modes
        import modules.checks.variable_checker as variable_checker
        import modules.updater as updater
        import modules.config.config_tools as conftools
        from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported

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
