import sys
import os
import shutil
import subprocess
from modules.versioning_tools import Version
from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW
from modules.config.configuration import local_version, remote_version

BACKUP_FOLDER_PREFIX = "version-"


def ensure_remote() -> None:
    remotes = subprocess.check_output(["git", "remote"]).decode().split()
    if "origin" not in remotes:
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/PowerPCFan/hardwareswap-listing-scraper.git"], check=True)  # noqa: E501


def create_backup(local_version: Version) -> None:
    backup_folder = f"{BACKUP_FOLDER_PREFIX}{local_version}-backup"
    os.makedirs(backup_folder, exist_ok=True)

    for item in os.listdir("."):
        if item == backup_folder or item.startswith(BACKUP_FOLDER_PREFIX):
            continue  # Skips backup folders

        if os.path.isdir(item):
            shutil.copytree(item, os.path.join(backup_folder, item), dirs_exist_ok=True)
        else:
            shutil.copy2(item, os.path.join(backup_folder, item))

    print(f"{GREEN}Backup created at {backup_folder}{RESET}")


def update_repo() -> None:
    ensure_remote()  # ensures that the remote is set up correctly to my github repo

    # git fetch origin
    subprocess.run(["git", "fetch", "origin"], check=True)
    # git reset --hard origin/main
    subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)

    print(f"{GREEN}Update Successful!{RESET}\nPlease restart HardwareSwap Listing Scraper.")
    sys.exit(0)


def check_for_updates() -> None:
    print(f"\n{BLUE}Checking for updates...{RESET}")

    try:
        # remote_version = versioning_tools.get_remote_version()
        # local_version = versioning_tools.get_local_version()

        if remote_version > local_version:
            print(f"{YELLOW}Update available: {local_version} → {remote_version}. Updating...{RESET}")

            if shutil.which(cmd="git") is None:
                print(f"{RED}Error: Git is not installed or is not in PATH. Update could not be downloaded.{RESET}")
                sys.exit(1)

            create_backup(local_version)
            update_repo()
        elif remote_version < local_version:
            print(f"{YELLOW}WARNING: Local version {local_version} is newer than remote version {remote_version}. If this is unintentional, you may experience issues.{RESET}\n")  # noqa: E501
        else:
            print(f"{GREEN}Script is already up to date.{RESET}.\n")
    except Exception as e:
        print(f"{RED}Error: Update failed:{RESET} {e}")
