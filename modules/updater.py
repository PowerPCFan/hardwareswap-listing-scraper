import sys
import os
import shutil
import subprocess
import requests
from packaging.version import Version
from modules.ansi import ansi_supported, ansi_codes

RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE = ansi_codes() if ansi_supported() else ("",) * 11

BACKUP_FOLDER_PREFIX = "version-"

def get_local_version():
    with open("version.txt", "r") as f:
        return Version(f.read().strip())
    
def get_remote_version():
    response = requests.get("https://raw.githubusercontent.com/PowerPCFan/hardwareswap-listing-scraper/refs/heads/main/version.txt", timeout=10)
    response.raise_for_status()
    return Version(response.text.strip())

def ensure_remote():
    remotes = subprocess.check_output(["git", "remote"]).decode().split()
    if "origin" not in remotes:
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/PowerPCFan/hardwareswap-listing-scraper.git"], check=True)

def create_backup(local_version):
    backup_folder = f"{BACKUP_FOLDER_PREFIX}{local_version}-backup"
    os.makedirs(backup_folder, exist_ok=True)

    for item in os.listdir("."):
        if item == backup_folder or item.startswith(BACKUP_FOLDER_PREFIX):
            continue # Skips backup folders

        if os.path.isdir(item):
            shutil.copytree(item, os.path.join(backup_folder, item), dirs_exist_ok=True)
        else:
            shutil.copy2(item, os.path.join(backup_folder, item))
            
    print(f"{GREEN}Backup created at {backup_folder}{RESET}")

def update_repo():
    ensure_remote() # ensures that the remote is set up correctly to my github repo

    # git fetch origin
    subprocess.run(["git", "fetch", "origin"], check=True)
    # git reset --hard origin/main
    subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
    
    print(f"{GREEN}Update Successful!{RESET}\nPlease restart HardwareSwap Listing Scraper.")
    sys.exit(0)

def check_for_updates():
    print(f"\n{BLUE}Checking for updates...{RESET}")
    
    try:
        remote_version = get_remote_version()
        local_version = get_local_version()
        
        if remote_version > local_version:
            print(f"{YELLOW}Update available: {local_version} → {remote_version}. Updating...{RESET}")
            
            if shutil.which("git") is None:
                print(f"{RED}Error: Git is not installed or is not in PATH. Update could not be downloaded.{RESET}")
                sys.exit(1)
            
            create_backup(local_version)
            update_repo()
        elif remote_version < local_version:
            print(f"{YELLOW}WARNING: Local version {local_version} is newer than remote version {remote_version}. If this is unintentional, you may experience issues.{RESET}\n")
        else:
            print(f"{GREEN}Script is already up to date.{RESET}\n")
    except Exception as e:
        print(f"{RED}Error: Update failed:{RESET} {e}")
