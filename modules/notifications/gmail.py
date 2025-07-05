import smtplib
import ssl
from email.message import EmailMessage
from typing import Optional

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

class Gmail:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str, html: Optional[str] = None):
        """
        :param recipient: Recipient's email address.
        :param subject: Email subject line.
        :param body: Plain text content of the email.
        :param html: Optional HTML version of the email.
        """
        msg = self._build_message(recipient, subject, body, html)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(self.email, self.password)
            server.send_message(msg)

    def _build_message(self, to: str, subject: str, body: str, html: Optional[str] = None) -> EmailMessage:
        msg = EmailMessage()
        msg["From"] = self.email
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content(body)

        if html:
            msg.add_alternative(html, subtype="html")

        return msg
