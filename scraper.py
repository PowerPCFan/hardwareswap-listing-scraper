#!/usr/bin/env python3

# Check if third party modules are installed and if not, install them
import modules.checks.dependency_checker as depchecker

# dont ask why there are two `if __name__ == "__main__"` statements lol
if __name__ == "__main__": depchecker.check_dependencies()

# stdlib imports
import sys

# local imports
import modules.welcome as welcome
import locales.keys as t
import modules.reddit as reddit
import modules.modes as modes
import modules.checks.variable_checker as variable_checker
import modules.updater as updater
import modules.config.config_tools as conftools
from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported
from modules.config.configuration import config

def main():
    conftools.convert_py_to_json()
    conftools.ensure_all_values_are_present()

    updater.check_for_updates()
    variable_checker.check()
    subreddit = reddit.initialize()
    welcome.print_welcome_text()

    match config.mode:
        case "firehose":
            modes.firehose(subreddit)
        case "match":
            modes.match(subreddit)
        case "match_llm":
            modes.match_llm(subreddit)
        case _:
            raise Exception(t.mode_is_invalid(mode=config.mode))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{YELLOW}\nExiting...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{'-' * 36}\n{RED}{t.unexpected_error()}{RESET}\n{'-' * 36}\n{e}")
        sys.exit(1)
