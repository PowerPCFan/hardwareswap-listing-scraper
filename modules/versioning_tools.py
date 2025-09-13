from packaging.version import Version
import requests
import random
import string


def create_cache_buster() -> str:
    random_string_4c: str = ''.join(random.choices(string.ascii_letters, k=4))
    random_string_8c: str = ''.join(random.choices(string.ascii_letters, k=8))

    random_string_4c = random_string_4c.lower()
    random_string_8c = random_string_8c.lower()

    return f"?{random_string_4c}={random_string_8c}"


def get_local_version():
    with open("version.txt", "r") as f:
        return Version(f.read().strip())


def get_remote_version():
    url = f"https://raw.githubusercontent.com/PowerPCFan/hardwareswap-listing-scraper/refs/heads/main/version.txt{create_cache_buster()}"  # noqa: E501
    print(url)
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return Version(response.text.strip())
