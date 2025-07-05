import requests
from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported

class TinyURL:
    def __init__(self):
        pass
    
    def shorten(self, url, timeout) -> str:
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
    def __init__(self):
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
        
    def shorten(self, url, timeout):
        try:
            response = requests.post(self.api, json={"url": url}, headers=self.headers, timeout=timeout)
            if response.status_code == 200:
                json = response.json()
                return json.get("short_url", url)
            else:
                raise Exception("Error shortening URL.")
        except Exception as e:
            print(f"{RED}ERROR: {e}{RESET}")
            return url

class SLPowerPCFanXYZ:
    def __init__(self):
        self.api = "https://sl.powerpcfan.xyz/api/shorten"
        # These headers are probably not necessary but I just included them because yes
        self.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "priority": "u=1, i",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://sl.powerpcfan.xyz/"
        }
        
    def shorten(self, url, timeout):
        try:
            response = requests.post(self.api, json={"url": url}, headers=self.headers, timeout=timeout)
            if response.status_code == 200:
                json = response.json()
                short = json.get("short", url)
                if short == url:
                    return short
                else:
                    return f"https://sl.powerpcfan.xyz{short}"
            else:
                raise Exception("Error shortening URL.")
        except Exception as e:
            print(f"{RED}ERROR: {e}{RESET}")
            return url
