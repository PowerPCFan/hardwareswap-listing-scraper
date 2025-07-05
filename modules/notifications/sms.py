from modules.notifications.gmail import Gmail
from modules.config.configuration import config


def send_sms(shorturl):
    gmail = Gmail(config.gmail_address, config.app_password)

    recipient = f"{config.phone_number}@{config.sms_gateway}"
    subject = "" # no subject
    body = f"New listing on r/hardwareswap: {shorturl}"

    gmail.send_email(recipient, subject, body)