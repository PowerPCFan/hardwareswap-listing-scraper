import requests
from modules.colors.ansi_codes import RESET, RED


class TinyURL:
    def __init__(self) -> None:
        pass

    def shorten(self, url: str, timeout: float | int) -> str:
        try:
            api_url = f"http://tinyurl.com/api-create.php?url={url}"
            response = requests.get(api_url, timeout=timeout)
            if response.status_code == 200:
                return response.text
            else:
                raise Exception("Error shortening URL.")
        except Exception as e:
            print(f"{RED}ERROR: {e}{RESET}")
            return url


class SLExpectOVH:
    def __init__(self) -> None:
        self.api = "https://sl.expect.ovh/api/shorten"
        # These headers are probably not necessary but I just included them because yes
        self.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "priority": "u=1, i",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "Referer": "https://www.whatdidyouexpect.eu/",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }

    def shorten(self, url: str, timeout: float | int) -> str:
        try:
            response = requests.post(self.api, json={"url": url}, headers=self.headers, timeout=timeout)
            if response.status_code == 200:
                json: dict = response.json()
                short_url: str = json.get("short_url", url)
                if short_url == url:
                    return url
                else:
                    return f"https://{short_url}"
            else:
                raise Exception("Error shortening URL.")
        except Exception as e:
            print(f"{RED}ERROR: {e}{RESET}")
            return url


class BlinkLink:
    def __init__(self) -> None:
        self.api = "https://blinkl.ink/api/shorten"
        # These headers are probably not necessary but I just included them because yes
        self.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "priority": "u=1, i",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
        }

    def shorten(self, url: str, timeout: float | int) -> str:
        try:
            response = requests.post(self.api, json={"url": url}, headers=self.headers, timeout=timeout)
            if response.status_code == 200:
                return response.json().get("short", url)
            else:
                raise Exception("Error shortening URL.")
        except Exception as e:
            print(f"{RED}ERROR: {e}{RESET}")
            return url
