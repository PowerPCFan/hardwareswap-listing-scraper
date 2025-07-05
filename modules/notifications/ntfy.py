import requests
from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported
from modules.config.configuration import config


def send_notification(text, shorturl):
    headers={
        "X-Click": shorturl, # notification click action
        "X-Title": f"New listing on r/hardwareswap",
        "X-Priority": "3", # 1 = min, 2 = low, 3 = default, 4 = high, 5 = max
        "X-Markdown": "yes"
    }

    data = f"{text}\n\nListing URL: [{shorturl}]({shorturl})"
    data = data.encode(encoding='utf-8')

    try:
        requests.post(
            "https://ntfy.sh/" + config.topic_name,
            data=data,
            headers=headers
        )
    # just some generic error handling for common requests errors:
    except requests.exceptions.ConnectionError as e:
        print(f"{RED}A network error while sending notification: {e}{RESET}")
    except requests.exceptions.Timeout:
        print(f"{RED}Request timed out while trying to send notification.{RESET}")
    except requests.exceptions.HTTPError as e:
        print(f"{RED}An HTTP error occurred while sending notification: {e}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}An unexpected error occurred while sending notification: {e}{RESET}")
    except Exception as e:
        print(f"{RED}An unexpected error occurred while sending notification: {e}{RESET}")