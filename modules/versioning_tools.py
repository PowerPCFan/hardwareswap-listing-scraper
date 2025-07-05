from packaging.version import Version
import requests

def get_local_version():
    
    with open("version.txt", "r") as f:
        return Version(f.read().strip())
    
def get_remote_version():
    
    response = requests.get("https://raw.githubusercontent.com/PowerPCFan/hardwareswap-listing-scraper/refs/heads/main/version.txt", timeout=10)
    response.raise_for_status()
    return Version(response.text.strip())