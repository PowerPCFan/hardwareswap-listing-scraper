import requests
from modules.systemd import Logger
from modules.colors.hex_colors import HTMLColor


def create_embed(
    color: str, url: str, author: str, trades: str, have: str, want: str,
    joined: str, post_karma: str, comment_karma: str, date_posted: str
) -> dict:

    embed_color: int | None = HTMLColor(color)

    return {
        "title": f"A new listing by u/{author} has been posted on r/HardwareSwap!",
        "url": url,
        "color": embed_color if embed_color is not None else int(0x3498db),

        "fields": [
            {
                "name": "User:",
                "value": f"[u/{author}](https://www.reddit.com/user/{author})",
                "inline": True
            },
            {
                "name": "User Info:",
                "value": (
                    f"- **{trades}** trades\n"
                    f"- Joined **{joined}**\n"
                    f"- **{post_karma}** post karma\n"
                    f"- **{comment_karma}** comment karma"
                ),
                "inline": False
            },
            {
                "name": "Has:",
                "value": have,
                "inline": False
            },
            {
                "name": "Wants:",
                "value": want,
                "inline": False
            },
            {
                "name": "Date Posted:",
                "value": f"{date_posted}",
                "inline": True
            }
        ],
        "thumbnail": {
            "url": "https://raw.githubusercontent.com/PowerPCFan/hardwareswap-listing-scraper/refs/heads/main/assets/3.png"  # noqa: E501
        },
    }


def send_webhook(webhook_url: str, content: str | None, embed: dict | None, username: str | None):
    logger = Logger()

    # Prepare the JSON payload
    json_data = {
        "content": content if content is not None else "",
        "embeds": [embed] if embed is not None else [],
        "username": username if username is not None else ""
    }

    # Send the webhook
    try:
        response = requests.post(webhook_url, json=json_data)
        if response.status_code not in [200, 204]:
            logger.failed(f"Failed to send webhook. Status code: {response.status_code}. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        logger.failed(f"Error sending webhook: {e}")
