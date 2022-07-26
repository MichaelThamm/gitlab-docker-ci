from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
import ssl
import cgi


class SmtpPackage(object):
    def __init__(self, **kwargs):
        self.smtp_server = kwargs['server']
        self.sender_email = kwargs['senderEmail']
        self.receiver_email = kwargs['recipientEmail']
        self.port = kwargs['port']
        if self.sender_email == "supp0rt.my.phish@gmail.com":
            self.password = "khdjwzwslrzudlue"
        self.message = None

    def smtpExecuteSend(self, amount=1):

        # Create a secure SSL context
        context = ssl.create_default_context()

        print('Sending ', end="", flush=True)
        for i in range(abs(amount)):
            try:
                server = smtplib.SMTP(self.smtp_server, self.port)
                server.ehlo()  # Can be omitted
                server.starttls(context=context)  # Secure the connection
                server.ehlo()  # Can be omitted
                server.login(self.sender_email, self.password)
                server.send_message(self.message)
                print('.', end="", flush=True)

            except Exception as e:
                print(f'This exception occured: {e}')

            finally:
                server.quit()

            if abs(amount) > 1 and i != abs(amount) - 1:
                time.sleep(10)  # sleep 3 seconds

        print('Your messages have been delivered')

    # Multipurpose Internet Mail Extensions
    def mimeMessageBuilder(self, form_dict):

        self.message = MIMEMultipart("alternative")
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
        self.message["Subject"] = "Automated Email From Website"

        # Create the plain-text and HTML version of your message
        text = f"""\
        Hi mike,

        {self.sender_email} sent you an email from your website.
        """

        message = self.messageHelper(form_dict)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(message, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.message.attach(part1)
        self.message.attach(part2)

    @staticmethod
    def messageHelper(form_dict):
        return f"""
        <html>
        <body>
        <p>
        This email is from {form_dict.get("Name")} via {form_dict.get("Email")}
        <br>
        <br>
        {form_dict.get("Message")}
        </p>
        </body>
        </html>"""


def run(form_dict):

    sender_email = "supp0rt.my.phish@gmail.com"
    recipient_email = "mikethamm44@gmail.com"

    # Port 465 for SSL || 587 for TLS || 1025 for local
    smtp_package = SmtpPackage(server="smtp.gmail.com",
                               senderEmail=sender_email, recipientEmail=recipient_email, port=587)

    smtp_package.mimeMessageBuilder(form_dict)
    smtp_package.smtpExecuteSend(amount=1)
